from rest_framework import serializers

from project.feed.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            **data,
            'restaurants_count': instance.restaurants.count(),
        }

    def create(self, validated_data):
        return Category.objects.create(
            **validated_data,
        )

