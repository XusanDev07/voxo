import uuid

from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.utils.services.normalize_text import normalize_text


@receiver(pre_save)
def general_pre_save(instance, *args, **kwargs):
    # ======= normalize CharField and TextField fields ===========
    normalize_text(obj=instance)
