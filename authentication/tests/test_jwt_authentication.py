from typing import (
    Dict,
)

from django.contrib.auth import get_user_model
from django.urls import reverse

from account.factories import UserFactory
from authentication.dataclasses import (
    AuthenticationDataclass,
    RefreshTokenDataclass,
)
from authentication.tests.base import BaseAuthenticationAPITestCase

User = get_user_model()


class TestJWTTokens(BaseAuthenticationAPITestCase):

    def setUp(self) -> None:
        self.user = UserFactory.create()

    def test_get_jwt_tokens(self):
        user_data = AuthenticationDataclass(
            email=self.user.email,
            password="FehKNot7",
        )
        response = self.do_post(user_data.dto)
        self.assertSuccess(response)
        self.assertJWTKeysExists(response)
        self.assertAccessJWTTokenData(response, self.user)

    def test_invalid_credentials(self):
        response = self.do_post()
        self.assertNotAuthenticated(response)

    def do_post(self, data: Dict = None):
        if data is None:
            data = AuthenticationDataclass().dto
        return super().do_post(data)

    @property
    def reverse(self):
        return reverse(
            "authentication:token",
        )


class TestRefreshJWTTokens(BaseAuthenticationAPITestCase):

    def setUp(self) -> None:
        self.user = UserFactory.create()

    def test_refresh_jwt_tokens(self):
        response = self.client.post(
            reverse("authentication:token"),
            data=AuthenticationDataclass(
                email=self.user.email,
                password="FehKNot7",
            ).dto,
            format="json",
        )
        self.assertSuccess(response)

        refresh_token = self.get_refresh_token(response)

        data = RefreshTokenDataclass(refresh=refresh_token).dto

        response = self.do_post(data)

        self.assertSuccess(response)
        self.assertJWTKeysExists(response)
        self.assertAccessJWTTokenData(response, self.user)

    @property
    def reverse(self):
        return reverse(
            "authentication:token-refresh",
        )
