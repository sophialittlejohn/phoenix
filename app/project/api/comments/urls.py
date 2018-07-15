from django.urls import path

from project.api.comments.views import CommentReviewView, DeleteReviewCommentView, LikeUnlikeReviewCommentView, \
    UserCommentsView

app_name = 'comments'

urlpatterns = [
    path('new/<int:review_id>/', CommentReviewView.as_view(), name='create_review_comment'),
    path('user/<int:user_id>/', UserCommentsView.as_view(), name='user_comments'),
    path('<int:review_id>/', DeleteReviewCommentView.as_view(), name='delete_review_comment'),
    path('like/<int:comment_id>/', LikeUnlikeReviewCommentView.as_view(), name='like_unlike_review_comment'),
]
