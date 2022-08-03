from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer, VoteSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    """The ViewSet for the Restaurant endpoint"""
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def dispatch(self, request, *args, **kwargs):
        if request.headers["app-version"] != "1.0"\
                and request.headers["app-version"] != "1.1":
            raise PermissionDenied('The app version should be 1.0 or 1.1')
        return super().dispatch(request, *args, **kwargs)

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)


class VoteViewSet(APIView):
    """The ViewSet for the Vote endpoint"""

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def dispatch(self, request, *args, **kwargs):
        if request.headers["app-version"] != "1.0"\
                and request.headers["app-version"] != "1.1":
            raise PermissionDenied('The app version should be 1.0 or 1.1')
        return super().dispatch(request, *args, **kwargs)

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
