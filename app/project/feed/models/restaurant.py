from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django_countries.fields import CountryField

from project.feed.models import Category


class Restaurant(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='restaurants',
        null=True,
    )

    name = models.CharField(
        verbose_name='restaurant_name',
        max_length=50,
    )

    # https://github.com/SmileyChris/django-countries/
    country = CountryField(blank_label='(select country)')

    street = models.CharField(
        verbose_name='restaurant_street',
        max_length=50,
    )

    city = models.CharField(
        verbose_name='restaurant_city',
        max_length=50,
    )

    zip = models.CharField(
        verbose_name='restaurant_zip',
        max_length=10,
        blank=True,
    )

    website = models.URLField(
        verbose_name='restaurant_website',
        # default length 200 is used
        blank=True,
    )

    # https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        verbose_name='restaurant_phone_number',
        validators=[phone_regex],
        max_length=15,
    )

    email = models.EmailField(
        verbose_name='restaurant_email',
        blank=True,
    )

    opening_hours = models.CharField(
        verbose_name='restaurant_opening_hours',
        max_length=50,
    )

    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    PRICE_LEVEL_CHOICES = (
        (LOW, '$'),
        (MEDIUM, '$$'),
        (HIGH, '$$$'),
    )

    price_level = models.CharField(
        verbose_name='restaurant_price_level',
        max_length=6,
        choices=PRICE_LEVEL_CHOICES,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='restaurants',
        null=True,
        blank=True,
    )

    created = models.DateTimeField(
        verbose_name='date_created',
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        verbose_name='date_modified',
        auto_now=True,
    )

    image = models.ImageField(
        verbose_name='restaurant_image',
        blank=True
    )

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'
