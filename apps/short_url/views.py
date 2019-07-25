from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from short_url.models import ShortUrl
from short_url.serializers import ShortUrlSerializer, ApplySerializer
from utils.exception import BadRequestError

User = get_user_model()


class ShortUrlViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'], permission_classes=[])
    def apply(self, request, *args, **kwargs):
        serializer = ApplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user, _ = User.objects.get_or_create(username=data['email'])
        ShortUrl.shorten(data['original_url'])
        # send_mail
        send_mail('标题', '内容', 'from@qq.com', ['to@qq.com'])
        return Response(status=status.HTTP_200_OK)
