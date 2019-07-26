from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.views import View
from django.shortcuts import render
from django.http import Http404
import json
import os
import re
from django.conf import settings

from short_url.models import ShortUrl
from short_url.serializers import ShortUrlSerializer, ApplySerializer
from short_url.email import send_apply_email

User = get_user_model()


class ShortUrlApply(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ApplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user, _ = User.objects.get_or_create(username=data['email'])
        short_url = ShortUrl.shorten(data['original_url'])
        send_apply_email(short_url.short_url, user.username)
        return Response(status=status.HTTP_200_OK)


class ShortUrlRead(View):
    template_name = 'resume.html'

    def get(self, request, token, *args, **kwargs):
        try:
            short_url = ShortUrl.objects.get(token=token, is_expired=False)
            short_url.is_expired = True
            short_url.save()
        except ShortUrl.DoesNotExist:
            raise Http404
        info = self.info_from_json()
        return render(request, self.template_name, context=info)

    @staticmethod
    def info_from_json():
        info_file = os.path.join(settings.BASE_DIR, 'info.json')
        with open(info_file, encoding='utf-8') as json_file:
            json_str = json_file.read()
            json_str = re.sub(r'`(.+?)`', r'<strong>\1</strong>', json_str)
            info = json.loads(json_str)
        return info


class ShortUrlViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
