# coding:       utf-8
# @Author:      u14e
# @Time:        2019/07/23 22:20
# @Description:
from decouple import config

# ==================== 用户相关 ==================== #
# 自定义用户Model
AUTH_USER_MODEL = 'user.User'

# ==================== Redis ==================== #
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SHORT_URL_PREFIX = 'https://u14e.xyz/short-url/resume'

# ==================== 邮箱配置 ==================== #
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_USER')          # 我的邮箱帐号
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')  # 授权码