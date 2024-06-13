
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #Django admin
    path('accounts/', include('django.contrib.auth.urls')), #user management
    path('', include('pages.urls')), #local apps
]
