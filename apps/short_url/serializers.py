# coding:       utf-8
# @Author:      u14e
# @Time:        2019/07/26 00:42
# @Description:
from rest_framework import serializers

from short_url.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortUrl
        fields = ['id', 'token', 'original_url', 'is_expired', 'created_at']


class ApplySerializer(serializers.Serializer):
    email = serializers.EmailField()
    original_url = serializers.CharField()