from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.db import models

ROLE_CHOICES = [
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Админ'),
]


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        max_length=254,
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        unique=True,
        max_length=150,
        validators=[UnicodeUsernameValidator()]
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=200,
        null=True
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=20,
        choices=ROLE_CHOICES,
        default='user'
    )
    date_joined = models.DateTimeField(
        verbose_name='Дата регистрации',
        null=True
    )
    bio = models.TextField(
        verbose_name='Биограффия',
        blank=True,
        null=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=50,
        null=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=50,
        null=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs) -> None:
        if self.is_superuser:
            self.role = 'admin'
        return super(User, self).save(*args, **kwargs)

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_moderator(self):
        return self.role == 'moderator'
