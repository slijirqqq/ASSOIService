from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from version.serializers import VersionSerializer
from version.version import get_api_version


class VersionAPIView(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    @staticmethod
    def list(request: Request):
        validated_version = VersionSerializer(
            data={
                "version": get_api_version()
            }
        )
        validated_version.is_valid(raise_exception=True)
        return Response(validated_version.data)
