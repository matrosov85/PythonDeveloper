"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from task2.views import ClassView, func_view
from task3.views import platform_view, games_view, cart_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func_url/', func_view),
    path('class_url/', ClassView.as_view()),
    path('platform/', platform_view),
    path('games/', games_view),
    path('cart/', cart_view)
]
