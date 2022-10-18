from django.urls import path

from version.views import (
    VersionAPIView,
)

urlpatterns = [
    path('version/', VersionAPIView.as_view({'get': 'list'}), name='api-version'),
]
