from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError, AuthenticationFailed


class IncorrectPasswordError(ValidationError):
    default_detail = _("Your old password was entered incorrectly. Please enter it again.")


class TokenInvalidOrExpired(AuthenticationFailed):
    default_detail = _("Token contained no recognizable user identification")


class UserNotFound(AuthenticationFailed):
    default_detail = _("User not found")
    default_code = "user_not_found"


class UserIsInActive(AuthenticationFailed):
    default_detail = _("User is inactive")
    default_code = "user_inactive"
