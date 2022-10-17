from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

latest_urlpatterns = [
    path('auth/', include(('authentication.urls', 'authentication'), namespace="authentication")),
    path('account/', include(('account.urls', 'account'), namespace="account")),
]

staticfiles_urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
media_files_urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(latest_urlpatterns), name='api'),
]

urlpatterns.extend(staticfiles_urlpatterns)
urlpatterns.extend(media_files_urlpatterns)
