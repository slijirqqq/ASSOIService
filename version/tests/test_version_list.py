from django.urls import reverse

from app_core.tests.base import BaseAPITestCase
from version.dataclasses import VersionDataclass
from version.serializers import VersionSerializer
from version.version import get_api_version


class TestVersionList(BaseAPITestCase):

    def test_success(self):
        response = self.get_version()
        self.assertSuccess(response)
        self.assertEqualVersion(response)

    def test_invalid(self):
        data = VersionDataclass(version="0.1")
        validated_version = VersionSerializer(data=data.dto)
        self.assertFalse(validated_version.is_valid(raise_exception=False))

        data = VersionDataclass(version="0.1.a")
        validated_version = VersionSerializer(data=data.dto)
        self.assertFalse(validated_version.is_valid(raise_exception=False))

    def get_version(self):
        return self.client.get(
            reverse(
                "version:api-version",
            )
        )

    def assertEqualVersion(self, response):
        version = response.json()["version"]
        file_version = get_api_version()
        self.assertEqual(version, file_version)
