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

CACHES['default']['OPTIONS']['PASSWORD'] = config('')
