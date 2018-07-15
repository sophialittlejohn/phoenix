from rest_framework.generics import ListAPIView

from project.api.categories.serializers import CategorySerializer
from project.feed.models import Category


class ListCategoriesView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def filter_queryset(self, queryset):
        return queryset
