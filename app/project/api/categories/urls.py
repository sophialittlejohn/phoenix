from django.urls import path

from project.api.categories.views import ListCategoriesView

app_name = 'categories'

urlpatterns = [
    path('list/', ListCategoriesView.as_view(), name='categories_list'),
]
