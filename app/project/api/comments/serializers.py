from rest_framework import serializers

from project.feed.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'review', 'content', 'modified', 'likes']
        read_only_fields = ['id', 'user', 'review', 'modified', 'likes']

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     return {
    #         **data,
    #         'restaurants_count': instance.restaurants.count(),
    #     }

    def create(self, validated_data):
        return Comment.objects.create(
            **validated_data,
            user=self.context.get('request').user,
            review=self.context.get('review')
        )

    def get_likes(self, comment):
        return comment.likes.count()
