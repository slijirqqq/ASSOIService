from typing import AnyStr, Dict

from django.conf import settings
from jwt import decode as jwt_decode
from rest_framework_simplejwt.settings import api_settings


class JWTDecoder:

    def __init__(self, jwt_token: AnyStr):
        self.__jwt_token = jwt_token

    def decode_jwt(self) -> Dict:
        decoded_jwt = jwt_decode(
            self.__jwt_token,
            key=settings.SECRET_KEY,
            algorithms=api_settings.defaults["ALGORITHM"],
        )
        return decoded_jwt
