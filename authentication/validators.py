from typing import AnyStr

import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework.exceptions import ValidationError


def validate_password(value: AnyStr):
    try:
        validators.validate_password(value)
    except exceptions.ValidationError as error:
        raise ValidationError(error.messages)
    return value
