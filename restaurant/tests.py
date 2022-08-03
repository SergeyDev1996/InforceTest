
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


RESTAURANT_URL = reverse("restaurant:restaurant-list")


class UnauthenticatedMovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.credentials(app='1.0')

    def test_auth_required(self):
        res = self.client.get(RESTAURANT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
