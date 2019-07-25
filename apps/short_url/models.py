from django.db import models
from django.utils import timezone
from libs.short_url import encode_url


class ShortUrl(models.Model):
    token = models.CharField(max_length=10,
                             unique=True,
                             db_index=True,
                             verbose_name='短网址 hash')
    original_url = models.CharField(max_length=10, verbose_name='源地址')
    is_expired = models.BooleanField(default=False, verbose_name='标识是否过期')
    created_at = models.DateTimeField(default=timezone.now)

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
    def shorten(cls, original_url):
        instance = cls.objects.create(original_url=original_url)
        instance.save()
