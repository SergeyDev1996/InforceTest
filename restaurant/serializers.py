from django.db import IntegrityError
from rest_framework import serializers
from datetime import datetime

from rest_framework.generics import get_object_or_404

from restaurant.models import Restaurant, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    day = datetime.today().weekday()
    days = {
        0: "menu_monday",
        1: "menu_tuesday",
        2: "menu_wednesday",
        3: "menu_thursday",
        4: "menu_friday",
        5: "menu_saturday",
        6: "menu_sunday"

    }
    day_of_the_week = days[day]
    menu = serializers.CharField(source=day_of_the_week, read_only=True)
    votes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Restaurant
        fields = ("name", "menu", "votes")


class RestaurantListSerializer(serializers.ModelSerializer):
    day = datetime.today().weekday()
    days = {
        0: "menu_monday",
        1: "menu_tuesday",
        2: "menu_wednesday",
        3: "menu_thursday",
        4: "menu_friday",
        5: "menu_saturday",
        6: "menu_sunday"

    }
    day_of_the_week = days[day]
    menu = serializers.CharField(source=day_of_the_week, read_only=True)
    votes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Restaurant
        fields = ("name", "menu", "votes")


class VoteSerializer(serializers.Serializer):
    restaurant = serializers.CharField()

    def create(self, validated_data):
        restaurant = get_object_or_404(Restaurant, name=validated_data["restaurant"])
        vote = Vote()
        vote.restaurant = restaurant
        try:
            vote.save(commit=False)
        except IntegrityError:
            return vote
        return vote

    class Meta:
        model = Vote
        exclude = ("id", "ip_address", "candidate")
