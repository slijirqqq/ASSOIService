from typing import AnyStr

from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.settings import api_settings

from authentication.exceptions import TokenInvalidOrExpired, UserNotFound, UserIsInActive

User = get_user_model()


class TokenMiddleware(MiddlewareMixin):

    def process_request(self, request) -> None:
        if request.user.is_anonymous:
            raw_token = request.headers.get('Authorization')
            if raw_token is None:
                return None
            else:
                validated_token = self.get_validated_token(raw_token.replace('Bearer ', ''))
            if validated_token is not None:
                request.user = self.get_user(validated_token)

    @staticmethod
    def process_response(request, response):
        return response

    @staticmethod
    def get_validated_token(raw_token: AnyStr):
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                return AuthToken(raw_token)
            except TokenError:
                continue
        return None

    @staticmethod
    def get_user(validated_token):
        user_id = validated_token.get(api_settings.USER_ID_CLAIM)
        if user_id is None:
            raise TokenInvalidOrExpired()
        try:
            user = User.objects.get(**{api_settings.USER_ID_FIELD: user_id})
        except User.DoesNotExist:
            raise UserNotFound()

        if not user.is_active:
            raise UserIsInActive()
        return user
