from django.urls import include, path
from rest_framework import routers

from ads.views import AdViewSet

# TODO настройка роутов для модели
router = routers.SimpleRouter()
router.register("ads", AdViewSet, basename="ads")


urlpatterns = [
    path("", include(router.urls))
]
