from django.contrib import admin
from django.urls import path, include

latest_urlpatterns = [
    path('auth/', include('authentication.urls'), name='authentication'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(latest_urlpatterns), name='api'),
]
