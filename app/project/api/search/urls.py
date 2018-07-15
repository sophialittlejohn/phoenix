from django.urls import path
from project.api.search.views import SearchAllView

app_name = 'search'

urlpatterns = [
    path('', SearchAllView.as_view(), name='search_all' )
]
