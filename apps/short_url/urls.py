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
    path('apply/', views.ShortUrlApply.as_view(), name='short_url_apply'),
    path('resume/<str:token>/', views.ShortUrlRead.as_view(), name='short_url_read')
]
