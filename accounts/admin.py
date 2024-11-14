from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User

admin.site.register(User) #Userモデルを登録
admin.site.unregister(Group) #Groupモデルは不要なので非表示

# Register your models here.
