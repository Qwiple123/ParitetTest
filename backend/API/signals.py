from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Image




@receiver(post_delete, sender=Image)
def delete_image_from_media(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)