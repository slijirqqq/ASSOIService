from django.urls import path

from authentication.views import (
    ASSOITokenObtainAPIView,
    ASSOITokenRefreshAPIView,
    RegistrationAPIView,
    PasswordChangeAPIView,
)

urlpatterns = [
    path('token/', ASSOITokenObtainAPIView.as_view(), name='token'),
    path('token/refresh/', ASSOITokenRefreshAPIView.as_view(), name='token-refresh'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('change_password/', PasswordChangeAPIView.as_view(), name='change-password'),
]
