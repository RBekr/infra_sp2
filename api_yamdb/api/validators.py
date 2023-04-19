import datetime as dt
import re

from django.core.exceptions import ValidationError
from rest_framework import serializers


def validate_score(value):
    MESSAGE = 'Оценка должна быть от 1 до 10'
    if 0 < value > 10:
        raise ValidationError(
            MESSAGE,
            params={'value': value},
        )
    return value


def title_year_validator(value):
    MESSAGE = 'Год публикации не может быть больше текущего: {}'
    year = dt.datetime.now().year
    if value > year:
        raise ValidationError(
            MESSAGE.format(year)
        )
    return value


def username_not_me(value):
    MESSAGE = 'Имя пользователя не может быть равно {}'
    if re.match(r'(?i)me', value) or value == '':
        raise serializers.ValidationError(
            MESSAGE.format(value)
        )
    return value
