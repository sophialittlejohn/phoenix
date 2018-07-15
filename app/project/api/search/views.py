from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from project.api.comments.serializers import CommentSerializer
from project.api.me.serializers import UserSerializer
from project.api.restaurant.serializers import RestaurantSerializer
from project.api.search.serializers import SearchSerializer
from project.feed.models import Restaurant, Comment

User = get_user_model()


class SearchAllView(APIView):
    authentication_classes = []

    def post(self, request, **kwargs):
        serializer = SearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        search_type = serializer.validated_data.get('type')
        search_string = serializer.validated_data.get('search_string')
        if search_type == 'restaurants':
            queryset = Restaurant.objects.filter(name__icontains=search_string)
            return Response(RestaurantSerializer(queryset, many=True).data)
        elif search_type == 'users':
            queryset = User.objects.all()
            queryset = queryset.filter(
                Q(username__contains=search_string) |
                Q(email__contains=search_string) |
                Q(first_name__contains=search_string) |
                Q(last_name__contains=search_string)
            )
            return Response(UserSerializer(queryset, many=True).data)
        else:
            queryset = Comment.objects.filter(content__icontains=search_string)
            return Response(CommentSerializer(queryset, many=True).data)
