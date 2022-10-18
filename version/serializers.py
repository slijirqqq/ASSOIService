from rest_framework import serializers

from app_core.serializers import SerializerImpl
from version.validators import validate_version


class VersionSerializer(SerializerImpl):
    version = serializers.CharField(
        validators=[
            validate_version,
        ],
    )
