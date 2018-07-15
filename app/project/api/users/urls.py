from django.urls import path

from project.api.users.views import ListUsersView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('list/', ListUsersView.as_view(), name='list_users'),
    path('', ListUsersView.as_view(), name='search_user'),
    path('<int:pk>/', UserProfileView.as_view(), name='user_profile')
]
