# coding:       utf-8
# @Author:      u14e
# @Time:        2019/07/26 10:57
# @Description:
from django.core.mail import send_mail
from django.conf import settings
import threading
import yagmail


def send_apply_email(short_url, recipient):
    t = threading.Thread(target=send_async_apply_email, args=(short_url, recipient))
    t.start()


def send_async_apply_email(short_url, recipient):
    subject = '简历地址 by u14e'
    message = '''
    Dear {recipient}:
        很开心能够来到这里,
        下面是我的在线简历的地址, 希望能够得到您的反馈(此链接地址只能访问一次, 请谨慎使用):
        {short_url}
    '''.format(recipient=recipient, short_url=short_url)

    if settings.DEBUG:
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])

    with yagmail.SMTP(user=settings.EMAIL_HOST_USER,
                      password=settings.EMAIL_HOST_PASSWORD,
                      host=settings.EMAIL_HOST) as yag:
        yag.send([recipient], subject, message)
