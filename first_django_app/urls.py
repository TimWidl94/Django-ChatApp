"""
URL configuration for first_django_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from chat.views import index, login__view, sign_up, logout_view
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', login__view, name='startingpage'),
    path('admin/', admin.site.urls),
    path('chat/', index),
    path('login/', login__view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', sign_up, name='sign_up'), 
    path('', include('django.contrib.auth.urls')),

]
