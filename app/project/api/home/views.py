from django.db.models import Count, Avg
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from project.api.home.serializers import ReviewSerializerScore
from project.feed.models import Review


class ListFourBestRatedRestaurants(GenericAPIView):
    queryset = Review.objects.filter(restaurant=1)
    # queryset = Review.objects.annotate(sum_ratings=Count('rating')).order_by('-sum_ratings')[:4]
    # queryset = Review.objects.all().aggregate(Avg('rating'))
    # queryset = Review.objects.annotate(rating_cnt=Count('rating'))

    serializer_class = ReviewSerializerScore

    def get(self, request, **kwargs):
        # the Serializer class takes an argument data that needs to be converted into a dict for passing in
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
