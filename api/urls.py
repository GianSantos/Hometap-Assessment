from rest_framework.routers import SimpleRouter

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('v1/', include('api.v1.urls')),
]
