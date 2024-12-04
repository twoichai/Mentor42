from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from .models import UserDetails


@receiver(post_save, sender=User)
def update_last_time_online(sender, instance, **kwargs):
    if instance.is_authenticated:
        # Create the UserDetails instance if it doesn't exist
        if not hasattr(instance, 'details'):
            UserDetails.objects.create(user=instance)

        # Update the last_time_online and is_online fields
        instance.details.last_time_online = now()
        instance.details.is_online = False  # Update dynamically as needed
        instance.details.save()
