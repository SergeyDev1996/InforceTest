
from django.urls import path, include
from rest_framework import routers

from restaurant.views import MenuViewSet, RestaurantViewSet, VoteViewSet

router = routers.DefaultRouter()
router.register("menu", MenuViewSet)
router.register("restaurant", RestaurantViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('vote/', VoteViewSet.as_view(), name='vote')
               ]

app_name = "restaurant"
