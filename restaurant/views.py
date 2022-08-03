from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from restaurant.models import Menu, Restaurant, Vote
from restaurant.serializers import MenuSerializer, RestaurantSerializer, RestaurantListSerializer, VoteSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return RestaurantListSerializer
        return RestaurantSerializer

class VoteViewSet(APIView):
    def post(self, request):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            created_instance = serializer.create(validated_data=request.data)
            created_instance.save()
            return Response(
                {
                    "message": "Vote cast successful"
                },
                status=status.HTTP_200_OK
            )
