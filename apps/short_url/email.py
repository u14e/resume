# coding:       utf-8
# @Author:      u14e
# @Time:        2019/07/26 10:57
# @Description:
from django.core.mail import send_mail
from django.conf import settings
import yagmail
import threading

yag = yagmail.SMTP(user=settings.EMAIL_USER,
                   password=settings.EMAIL_PASSWORD,
                   host=settings.EMAIL_HOST)


def send_apply_email(short_url, recipient):
    t = threading.Thread(target=send_async_apply_email, args=(short_url, recipient))
    t.start()


def send_async_apply_email(short_url, recipient):
    subject = '短链接地址'
    message = '''
    Dear {recipient}:
        首先非常感谢您能够尝试,
        下面是我的在线简历的地址, 希望能够得到您的反馈:
        {short_url}
    '''.format(recipient=recipient, short_url=short_url)
    if settings.DEBUG:
        send_mail(subject, message, settings.EMAIL_USER, [recipient])
    else:
        yag.send([recipient], subject, message)
