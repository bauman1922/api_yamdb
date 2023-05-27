import re

from django.core.exceptions import ValidationError


def validate_username(value):
    if value.lower() == 'me':
        raise ValidationError(
            'Введите другое имя пользователя'
        )
    if not bool(re.match(r'^[\w.@+-]+$', value)):
        raise ValidationError(
            'Некорректные символы в username'
        )
    return value


def validate_email(value):
    if value.lower() == '':
        raise ValidationError(
            'Это поле обязательно должно быть заполненно'
        )
    return value
