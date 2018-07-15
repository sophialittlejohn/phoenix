from rest_framework import serializers


class SearchSerializer(serializers.Serializer):

    type = serializers.CharField(
        allow_blank=False
    )
    search_string = serializers.CharField(
        allow_blank=False
    )
