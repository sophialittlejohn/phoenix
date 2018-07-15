from rest_framework import serializers

from project.feed.models import Review


class ReviewSerializerScore(serializers.ModelSerializer):
    # id = serializers.CharField(
    #     required=False
    # )
    # restaurant = serializers.CharField(
    #     label='restaurant',
    # )
    # content = serializers.CharField(
    #     label='content',
    # )
    # rating = serializers.EmailField(
    #     label='rating',
    # )
    # ratings_avg = serializers.IntegerField(
    #     source='rating_set.avg',
    #     read_only=True
    # )
    restaurant = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    # def to_representation(self, instance):
    #     return {'id': instance.pk, 'rating_cnt': instance.rating_cnt}

    class Meta:
        model = Review
        fields = ['id', 'user', 'restaurant', 'content', 'rating', 'comments']
        read_only_fields = ['id', 'user', 'restaurant', 'comments']
