import random

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


def code_generator(length=6):
    numbers = '0123456789'
    return ''.join(random.choice(numbers) for i in range(length))


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
    )

    location = models.CharField(
        verbose_name='user_location',
        max_length=30,
    )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        verbose_name='user_phone_number',
        validators=[phone_regex],
        max_length=15,
    )

    things_love = models.TextField(
        verbose_name='things_user_love',
    )

    description = models.TextField(
        verbose_name='user_description',
    )

    image = models.ImageField(
        blank=True
    )

    registration_code = models.CharField(
        verbose_name='registration_code',
        max_length=15,
        default=code_generator,
    )
