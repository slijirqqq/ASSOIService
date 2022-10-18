from django.urls import re_path

from api_doc.views import schema_view

urlpatterns = [
    re_path(r'^doc/$', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema-ui'),
]
