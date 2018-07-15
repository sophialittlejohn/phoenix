from django.conf import settings
from django.db import models
from rest_framework.compat import MaxValueValidator, MinValueValidator

from project.feed.models import Restaurant


class Review(models.Model):

    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        related_name='reviews',
        on_delete=models.SET_NULL,
        null=True,
    )

    restaurant = models.ForeignKey(
        Restaurant,
        related_name='reviews',
        on_delete=models.CASCADE,
    )

    content = models.TextField(
        verbose_name='review_content',
    )

    rating = models.IntegerField(
        verbose_name='restaurant_rating',
        validators=[MaxValueValidator(5), MinValueValidator(1)]
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
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-modified']
        unique_together = [(
             'user', 'restaurant'
        )]
