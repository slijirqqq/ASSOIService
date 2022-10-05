from django.urls import path

from authentication.views import (
    ASSOITokenObtainAPIView,
    ASSOITokenRefreshAPIView
)

urlpatterns = [
    path('token/', ASSOITokenObtainAPIView.as_view(), name='token'),
    path('token/refresh/', ASSOITokenRefreshAPIView.as_view(), name='token-refresh'),
]
