from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from accounts.models import User
import random

# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)

def random_url():
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    url = ''.join(random.choice(chars)for i in range(16))
    return url

# class Post(models.Model):
#     content = models.TextField(max_length=50)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_posted = models.DateTimeField(default=timezone.now)
#     likes = models.IntegerField(default=0)
#     dislikes = models.IntegerField(default=0)
    
#     def __str__(self):
#         return self.content[:10]
# # Create your models here.

# models.py (アプリケーション名: contributionApp)

class Point(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=255)
    description = models.TextField()
    points_requested = models.PositiveIntegerField()
    date = models.DateField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # カスタムユーザーモデルに対応
        on_delete=models.CASCADE,
        related_name="points"
    )


    def __str__(self):
        return f"{self.activity_name} - {self.user.account_id}"
