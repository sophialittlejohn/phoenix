from django.urls import path

from project.api.me.views import GetUpdateUserProfileView

app_name = 'me'

urlpatterns = [
    path('', GetUpdateUserProfileView.as_view(), name='user_profile')
]
