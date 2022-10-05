from rest_framework_simplejwt.serializers import (
    TokenObtainSerializer
)

from app_core.serializers import SerializersImplMixin


class ASSOITokenObtainSerializer(SerializersImplMixin, TokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.get_username()

        return token
