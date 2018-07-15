from django.contrib.auth.models import User
from django.db import models

from project.feed.models import Review


class Comment(models.Model):

    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True,
    )

    review = models.ForeignKey(
        Review,
        related_name='comments',
        on_delete=models.CASCADE,
    )

    content = models.TextField(
        verbose_name='review_comment',
    )

    created = models.DateTimeField(
        verbose_name='date_created',
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        verbose_name='date_modified',
        auto_now=True,
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-modified']
