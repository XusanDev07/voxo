import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.utils.models.base_model import AbstractBaseModel


class CustomUser(AbstractBaseModel, AbstractUser):
    """ Custom user model """

    region = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)