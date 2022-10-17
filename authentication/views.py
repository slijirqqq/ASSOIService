from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from authentication.serializers import (
    RegistrationSerializer,
    PasswordChangeSerializer, ASSOITokenObtainPairSerializer,
)

User = get_user_model()


class ASSOITokenObtainAPIView(TokenObtainPairView):
    serializer_class = ASSOITokenObtainPairSerializer


class ASSOITokenRefreshAPIView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer


class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer


class PasswordChangeAPIView(UpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = PasswordChangeSerializer

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
