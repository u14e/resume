from django.db import models
from django.utils import timezone
from libs.short_url import encode_url
from django.conf import settings


class ShortUrl(models.Model):
    token = models.CharField(max_length=10, db_index=True, verbose_name='短网址 hash')
    original_url = models.CharField(max_length=100, verbose_name='源地址')
    is_expired = models.BooleanField(default=False, verbose_name='标识是否过期')
    created_at = models.DateTimeField(default=timezone.now)
    expired_at = models.DateTimeField(null=True, blank=True, verbose_name='过期时间')
    created_by = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = '短网址'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.pk and not self.token:
            self.token = encode_url(self.pk)
        super().save(*args, **kwargs)
        if not self.token:
            self.save()

    @classmethod
    def shorten(cls, original_url, **kwargs):
        instance = cls.objects.create(original_url=original_url, **kwargs)
        return instance

    @property
    def short_url(self):
        return '{}/{}/'.format(settings.SHORT_URL_PREFIX,
                               self.token)


class ShortUrlMessage(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']
