from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.api.base import GetObjectMixin
from project.api.categories.serializers import CategorySerializer
from project.api.permissions import IsUserOrReadOnly
from project.api.restaurant.serializers import RestaurantSerializer, RestaurantImageUploadSerializer
from project.feed.models import Restaurant, Category


class ListAllRestaurantsView(ListAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    def filter_queryset(self, queryset):
        search_string = self.request.query_params.get('search')
        if search_string:
            queryset = queryset.filter(Q(name__icontains=search_string) |
                                       Q(country__icontains=search_string) |
                                       Q(street__icontains=search_string) |
                                       Q(city__icontains=search_string)).order_by('reviews')
        return queryset


class NewRestaurantView(GenericAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        restaurant = serializer.create(serializer.validated_data)
        return Response(RestaurantSerializer(restaurant).data, status.HTTP_201_CREATED)


class RestaurantImageUploadView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, **kwargs):
        serializer = RestaurantImageUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Ok')


class RestaurantGetUpdateDeleteView(GenericAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [
        IsUserOrReadOnly,
    ]

    def get(self, request, **kwargs):
        restaurant = self.get_object()
        serializer = self.get_serializer(restaurant)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, **kwargs):
        restaurant = self.get_object()
        serializer = self.get_serializer(restaurant, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, request, **kwargs):
        restaurant = self.get_object()
        restaurant.delete()
        return Response('Deleted', status.HTTP_200_OK)


class ListCategoryRestaurantsView(GetObjectMixin, ListAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    def filter_queryset(self, queryset):
        category = self.get_object_by_model(Category, pk=self.kwargs.get('pk'))
        return queryset.filter(category=category)


class UserRestaurantsView(ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.filter(user__username=self.request.user.username).order_by('created')
