from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "My Site"
admin.site.site_title = "My_site"

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('core.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)