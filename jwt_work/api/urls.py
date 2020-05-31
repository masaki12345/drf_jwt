from django.urls import include, path
from rest_framework import routers
from .views import MainContentViewSet,TagViewSet


router = routers.DefaultRouter()

router.register('maincontent',MainContentViewSet)
router.register('tag',TagViewSet)


urlpatterns = [
    path('',include(router.urls))
]
