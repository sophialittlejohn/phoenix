from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.api.base import GetObjectMixin
from project.api.permissions import IsUserOrReadOnly
from project.api.reviews.serializers import ReviewSerializer
from project.feed.models import Restaurant, Review, ReviewLike


class NewReviewView(GetObjectMixin, GenericAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, **kwargs):
        restaurant = self.get_object_by_model(Restaurant, pk=self.kwargs.get('pk'))
        request.restaurant = restaurant
        serializer = self.get_serializer(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        new_review = serializer.create(serializer.validated_data)
        return Response(ReviewSerializer(new_review).data, status.HTTP_201_CREATED)


class RestaurantReviewsView(GetObjectMixin, ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def filter_queryset(self, queryset):
        restaurant = self.get_object_by_model(Restaurant, pk=self.kwargs.get('pk'))
        return queryset.filter(restaurant=restaurant)


class UserReviewsView(ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(user__username=self.request.user.username)


class ReviewGetUpdateDeleteView(GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        IsUserOrReadOnly,
    ]

    def get(self, request, **kwargs):
        review = self.get_object()
        serializer = self.get_serializer(review)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, **kwargs):
        review = self.get_object()
        serializer = self.get_serializer(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, request, **kwargs):
        review = self.get_object()
        review.delete()
        return Response('Deleted')


class LikeUnlikeReviewView(GetObjectMixin, APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, review_id):
        review = self.get_object_by_model(Review, review_id)
        try:
            ReviewLike.objects.create(user=request.user, review=review)
        except ReviewLike.DoesNotExist:
            raise Http404
        return Response('Review liked!')

    def delete(self, request, review_id):
        review = self.get_object_by_model(Review, review_id)
        ReviewLike.objects.get(user=request.user, review=review).delete()
        return Response('Review unliked!')


class LikedReviewsView(GetObjectMixin, APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        reviews = Review.objects.filter(likes__user=request.user)
        return Response(ReviewSerializer(reviews, many=True).data, status.HTTP_200_OK)


class CommentedReviewsView(GetObjectMixin, APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        reviews = Review.objects.filter(comments__user=request.user)
        return Response(ReviewSerializer(reviews, many=True).data, status.HTTP_200_OK)
