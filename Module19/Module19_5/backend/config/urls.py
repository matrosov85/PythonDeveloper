from django.contrib import admin
from django.urls import path

from task1.views import platform_view, games_view, cart_view, news_view, sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/', platform_view),
    path('platform/games/', games_view),
    path('platform/cart/', cart_view),
    path('platform/news/', news_view),
    path('', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django),
]
