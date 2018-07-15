from django.urls import path

from project.api.reviews.views import NewReviewView, RestaurantReviewsView, UserReviewsView, ReviewGetUpdateDeleteView, \
    LikeUnlikeReviewView, LikedReviewsView, CommentedReviewsView

app_name = 'reviews'

urlpatterns = [
    path('new_review/<int:pk>/', NewReviewView.as_view(), name='new_review'),
    path('restaurant/<int:pk>/', RestaurantReviewsView.as_view(), name='restaurant_reviews'),
    path('user/<int:pk>/', UserReviewsView.as_view(), name='user_reviews'),
    path('<int:pk>/', ReviewGetUpdateDeleteView.as_view(), name='review_get_update_delete'),
    path('like/<int:review_id>/', LikeUnlikeReviewView.as_view(), name='like_unlike_review'),
    path('likes/', LikedReviewsView.as_view(), name='liked_reviews'),
    path('comments/', CommentedReviewsView.as_view(), name='commented_reviews'),
]
