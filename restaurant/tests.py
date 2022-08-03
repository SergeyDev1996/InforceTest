from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer

RESTAURANT_URL = reverse("restaurant:restaurant-list")


def sample_restaurant(**params):
    defaults = {
        "name": "StarBucks",
    }
    defaults.update(params)

    return Restaurant.objects.create(**defaults)


class UnauthenticatedRestaurantApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.credentials(app='1.0')

    def test_auth_required(self):
        res = self.client.get(RESTAURANT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedRestaurantApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "testpass",
        )
        self.client.force_authenticate(self.user)

    def test_list_of_restaurants(self):
        sample_restaurant()

        res = self.client.get(RESTAURANT_URL)

        movies = Restaurant.objects.all().order_by("id")
        serializer = RestaurantSerializer(movies, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
