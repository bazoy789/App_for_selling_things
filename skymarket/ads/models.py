from datetime import datetime

from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=100, null=True)
    price = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=500, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]

    def __str__(self):
        return self.text
