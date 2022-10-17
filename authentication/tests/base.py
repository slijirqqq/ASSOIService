from typing import (
    Union,
    AnyStr,
    Dict,
)

from app_core.tests.base import BaseAPITestCase
from app_core.utils import JWTDecoder


class BaseAuthenticationAPITestCase(BaseAPITestCase):

    def do_post(self, data: Dict = None):
        return self.client.post(
            self.reverse,
            data=data,
            format="json",
        )

    @property
    def reverse(self):
        raise NotImplementedError()

    @staticmethod
    def get_access_token(response) -> Union[AnyStr, None]:
        return response.json().get("access")

    @staticmethod
    def get_refresh_token(response) -> Union[AnyStr, None]:
        return response.json().get("refresh")

    def assertJWTKeysExists(self, response):
        ordering_keys = ["refresh", "access"]
        response_keys = sorted(list(response.json().keys()), reverse=True)
        self.assertListEqual(response_keys, ordering_keys)

    def assertAccessJWTTokenData(self, response, user):
        access_token = self.get_access_token(response)
        decoder = JWTDecoder(access_token)
        jwt_data = decoder.decode_jwt()

        self.assertEqual(user.id, jwt_data.get("user_id"))
        self.assertEqual(user.email, jwt_data.get("email"))
        self.assertListEqual(
            list(user.groups.all().values_list("name", flat=True)),
            jwt_data.get("roles"),
        )
