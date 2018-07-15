from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project.api.base import GetObjectMixin
from project.api.comments.serializers import CommentSerializer
from project.api.reviews.serializers import ReviewSerializer
from project.feed.models import Review, Comment, CommentLike


class CommentReviewView(GetObjectMixin, APIView):

    def post(self, request, review_id):
        review = self.get_object_by_model(Review, review_id)
        serializer = CommentSerializer(data=request.data, context={'request': request,
                                                                   'reviews': review})
        serializer.is_valid(raise_exception=True)
        new_comment = serializer.create(serializer.validated_data)
        # try:
        #     Comment.objects.create(user=request.user, reviews=reviews)
        # except Comment.DoesNotExist:
        #     raise Http404

        return Response(CommentSerializer(new_comment).data, status.HTTP_201_CREATED)


class DeleteReviewCommentView(GetObjectMixin, APIView):

    def delete(self, request, review_id):
        review = self.get_object_by_model(Review, review_id)
        review.comments.get(user=request.user).delete()
        return Response('Comment deleted!')


class LikeUnlikeReviewCommentView(GetObjectMixin, APIView):

    def post(self, request, comment_id):
        comment = self.get_object_by_model(Comment, comment_id)
        try:
            CommentLike.objects.create(user=request.user, comment=comment)
        except CommentLike.DoesNotExist:
            raise Http404
        return Response('Comment liked!')

    def delete(self, request, comment_id):
        comment = self.get_object_by_model(Comment, comment_id)
        CommentLike.objects.get(user=request.user, comment=comment).delete()
        return Response('Comment unliked!')


class UserCommentsView(GetObjectMixin, APIView):

    def get(self, request, user_id):
        user = self.get_object_by_model(User, user_id)
        comments = user.comments.all()
        return Response(CommentSerializer(comments, many=True).data, status.HTTP_200_OK)
