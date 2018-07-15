from django.urls import path

from project.api.home.views import ListFourBestRatedRestaurants


app_name = 'home'

urlpatterns = [
    path('', ListFourBestRatedRestaurants.as_view(), name='home'),
]
