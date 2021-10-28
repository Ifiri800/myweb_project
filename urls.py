"""myweb_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import UserSettingsHolder
from django.contrib import  admin
from rest_framework.authtoken import views
from django.urls import path, include
import rest_framework 
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path ('admin', admin.site.urls),
    path('api_auth/', include(rest_framework)),
    path('api/token/', obtain_auth_token, name='obtain'),
    path('api-token-auth/', views.obtain_auth_token),
    path('likes/<int:post_id', UserSettingsHolder, name='likes')
    
]