from django.conf import settings
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from version.version import get_api_version

permission_classes = [
    permissions.IsAdminUser,
]

if settings.DEBUG:
    permission_classes = [
        permissions.AllowAny,
    ]

api_info = openapi.Info(
    title=_("ASSOI API"),
    default_version=get_api_version(),
    description=_("ASSOI cathedral API for employees of KSTU"),
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact("ruslan.torbeev@yandex.ru"),
    license=openapi.License("MIT License"),
)

schema_view = get_schema_view(
    info=api_info,
    public=False,
    permission_classes=permission_classes,
)
