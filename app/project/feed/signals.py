from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from project.feed.models import Profile


@receiver(post_save, sender=User)
def my_handler(**kwargs):
    user = kwargs.get('instance')
    Profile.objects.get_or_create(
        user=user,
    )
