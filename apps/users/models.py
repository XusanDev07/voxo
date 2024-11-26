from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.utils.models.base_model import AbstractBaseModel


class CustomUser(AbstractBaseModel, AbstractUser):
    region = models.PositiveSmallIntegerField(blank=True, null=True)
    district = models.PositiveSmallIntegerField(blank=True, null=True)
