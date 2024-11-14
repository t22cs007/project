from django.db import models
from django.contrib.auth.models import (BaseUserManager,
                                        AbstractBaseUser,
                                        PermissionsMixin)
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def _create_user(self,email,account_id,password,**extra_firlds):
        email = self.normalize_email(email)
        user = self.model(email=email, account_id=account_id, **extra_firlds)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_user(self,email,account_id,password=None, **extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',False)
        extra_firlds.setdefault('is_superuser',False)
        return self._create_user(
            email=email,
            account_id=account_id,
            password=password,
            **extra_fields,
        )
        
    def create_superuser(self,email,account_id,password,**extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            account_id=account_id,
            password=password,
            **extra_fields,
        )
        
class User(AbstractBaseUser,PermissionsMixin):
    account_id = models.CharField(
        verbose_name=_("account_id"),
        unique=True,
        max_length=10
    )
    email = models.EmailField(
        verbose_name=_("email"),
        unique=True
    )
    first_name = models.CharField(
        verbose_name=_("first_name"),
        max_length=150,
        null=True,
        blank=False
    )
    last_name = models.CharField(
        verbose_name=("last_name"),
        max_length=159,
        null=True,
        blank=False
    )
    birth_date = models.DateField(
        verbose_name=_("birth_date"),
        blank=True,
        null=True
    )
    is_superuser = models.BooleanField(
        verbose_name=_("is_superuser"),
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created_at"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated_at"),
        auto_now=True
    )
    objects = UserManager()
    
    USERNAME_FIELD = 'account_id' #ログインにはIDを使用
    REQUIRED_FIELDS = ['email'] #スーパーユーザーはemailも設定する
    
    def __str__(self):
        return self.account_id

# Create your models here.
