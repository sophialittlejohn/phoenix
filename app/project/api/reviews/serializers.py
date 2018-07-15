from rest_framework import serializers

from project.api.comments.serializers import CommentSerializer
from project.feed.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'restaurant', 'content', 'rating', 'comments']
        read_only_fields = ['id', 'user', 'restaurant', 'comments']

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     return {
    #         **data,
    #         'restaurants_count': instance.restaurants.count(),
    #     }

    def create(self, validated_data):
        return Review.objects.create(
            **validated_data,
            user=self.context.get('request').user,
            restaurant=self.context.get('request').restaurant
        )
