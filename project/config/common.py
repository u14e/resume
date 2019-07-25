# coding:       utf-8
# @Author:      u14e
# @Time:        2019/07/23 22:20
# @Description:

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
