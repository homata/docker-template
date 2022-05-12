from ast import Try
from operator import is_not
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core.mail import send_mail
import uuid as uuid_lib
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from typing import Any, Optional

"""
Notes
----
* [Django の認証方法のカスタマイズ](https://docs.djangoproject.com/ja/4.0/topics/auth/customizing/)
* [Django Custom User Model の作成](https://qiita.com/startours777/items/706d38e712b0c737a16a)
* [Django ユーザー カスタマイズ方法](https://qiita.com/okoppe8/items/10ae61808dc3056f9c8e)
* [Django 管理画面逆引きメモ](https://qiita.com/zenwerk/items/044c149d93db097cdaf8)
"""

class Department(models.Model):
    """所属 兼任可"""

    name = models.CharField(_('department'), max_length=150, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User"""

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    uuid = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)  # 管理ID
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    full_name = models.CharField(_('full name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True, blank=True, null=True)  # メールアドレス = これで認証する
    departments = models.ManyToManyField(
        Department,
        verbose_name=_('department'),
        blank=True,
        help_text=_('Specific Departments for this user.'),
        related_name="user_set",
        related_query_name="user",
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    is_superuser = models.BooleanField(default=False)  # 管理者権限
    date_joined = models.DateTimeField(default=timezone.now)  # アカウント作成日時
    password_changed = models.BooleanField(default=False)  # パスワードを変更したかどうかのフラグ
    password_changed_date = models.DateTimeField(blank=True, null=True)  # 最終パスワード変更日時

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email

    # 既存メソッドの変更
    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    ユーザ新規作成時、自動的にTOKENを発行する。
    """
    if created:
        Token.objects.create(user=instance)
