from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from authentication.serializers import ASSOITokenObtainSerializer


class ASSOITokenObtainAPIView(TokenObtainPairView):
    serializer_class = ASSOITokenObtainSerializer


class ASSOITokenRefreshAPIView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer
