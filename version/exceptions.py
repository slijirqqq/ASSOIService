from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _


class VersionDoesNotMatchSemVer(exceptions.ValidationError):
    default_detail = _("Version doesnt match SemVer, missed one of the version items.")


class VersionItemMustBeDigit(exceptions.ValidationError):
    default_detail = _("One of the version items doesnt digit")
