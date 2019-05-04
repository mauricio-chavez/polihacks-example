"""Polihacks URL Configuration"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', include('welcome.urls')),
    path('users/', include('users.urls')),
]
