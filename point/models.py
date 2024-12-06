from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date,timedelta
from django.utils.translation import gettext_lazy as _
from accounts.models import User
import random

from django.db import models

class Item(models.Model):
    TYPE_CHOICES = [
        ('food', '食べ物'),
        ('good', 'グッズ'),
        ('other', 'その他'),
        ('chiket', '食券'),
    ]
    
    name = models.CharField(max_length=255)  # 商品名
    point = models.IntegerField()           # ポイント
    image = models.ImageField(upload_to='item_images/')  # 商品画像
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)  # 商品カテゴリ

    def __str__(self):
        return self.name
    
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
from django.core.validators import MaxValueValidator,MinValueValidator

POINT_CHOICES = (
    (50,'50'),
    (100,'100'),
    (150,'150'),
    (200,'200'),
    (250,'250'),
    (300,'300'),
)

class Point(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=255)
    description = models.TextField()
    # points_requested = models.PositiveIntegerField(default=50,validators=[MinValueValidator(50),MaxValueValidator(300)])
    points_requested = models.PositiveIntegerField(verbose_name="ポイント",choices=POINT_CHOICES)
    date = models.DateField(default=date.today())
    # date = models.DateField(default=lambda: date.today()+timedelta(days=5))
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
