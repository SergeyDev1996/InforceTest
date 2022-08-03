
from django.urls import path, include
from rest_framework import routers

from restaurant.views import RestaurantViewSet, VoteViewSet

router = routers.DefaultRouter()
router.register("restaurant", RestaurantViewSet, basename="restaurant")

urlpatterns = [
    path("", include(router.urls)),
    path("vote/", VoteViewSet.as_view(), name="vote-api"),
]

app_name = "restaurant"
