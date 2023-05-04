from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter

user_route = SimpleRouter()

user_route.register('users', UserViewSet, basename="users")

urlpatterns = [
    path("", include(user_route.urls))
]
