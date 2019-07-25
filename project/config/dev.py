# coding:       utf-8
# @Author:      u14e
# @Time:        2019/07/23 20:26
# @Description:
from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'resume',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4'
        },
    }
}

# 控制台本地查看邮件发送信息
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
