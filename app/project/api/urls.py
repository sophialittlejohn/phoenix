from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('category/', include('project.api.categories.urls'), name='categories'),
    path('restaurants/', include('project.api.restaurant.urls'), name='restaurants'),
    path('reviews/', include('project.api.reviews.urls'), name='reviews'),
    path('comments/', include('project.api.comments.urls'), name='comments'),
    path('registration/', include('project.api.registration.urls'), name='registration'),
    path('users/', include('project.api.users.urls'), name='users'),
    path('me/', include('project.api.me.urls'), name='me'),
    path('auth/', include('project.api.auth.urls'), name='auth'),
    path('search/', include('project.api.search.urls'), name='search'),
    path('home/', include('project.api.home.urls'), name='home'),
]
