
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #Django admin
    path('accounts/', include('django.contrib.auth.urls')), #user management
    #local apps
    path('accounts/', include('accounts.urls')), 
    path('', include('pages.urls')), #local apps
]
