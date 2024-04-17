from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "My Site"
admin.site.site_title = "My_site"

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('core.urls')),
]
