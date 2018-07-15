from django.contrib.auth.models import User
from django.db import models

from project.feed.models import Comment, Review


class ReviewLike(models.Model):
    user = models.ForeignKey(
        User,
        related_name='review_likes',
        on_delete=models.SET_NULL,
        null=True,
    )

    review = models.ForeignKey(
        Review,
        related_name='likes',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Review like'
        verbose_name_plural = 'Review likes'
        unique_together = [(
             'user', 'review'
        )]


class CommentLike(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    comment = models.ForeignKey(
        Comment,
        related_name='likes',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'CommentLike'
        verbose_name_plural = 'Comment likes'
        unique_together = [(
             'user', 'comment'
        )]
