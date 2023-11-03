from django.urls import path, include
from .views import FilmView, FilmViewSet, RatingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("Film", FilmViewSet)
router.register("Rating", RatingViewSet)

urlpatterns = [
    path("first", FilmView.as_view()),
    path("serializer", include(router.urls))
]