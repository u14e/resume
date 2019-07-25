# coding:       utf-8
# @Author:      u14e
# @Time:        2019/07/23 23:06
# @Description:
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from short_url import views

router = DefaultRouter()
router.register(r'', views.ShortUrlViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
