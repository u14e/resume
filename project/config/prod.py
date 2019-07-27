# coding:       utf-8
# @Author:      u14e
# @Time:        2019/07/23 20:26
# @Description:
from .common import *
from decouple import config


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4'
        },
    }
}

# CACHES['default']['OPTIONS']['PASSWORD'] = config('REDIS_PASSWORD')

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = 25
# EMAIL_HOST_USER = config('EMAIL_USER')          # 我的邮箱帐号
# EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')  # 授权码
# EMAIL_USE_TLS = True    # 开启安全链接
# DEFAULT_FROM_EMAIL = SERVER_EMAIL = EMAIL_HOST_USER  # 设置发件人