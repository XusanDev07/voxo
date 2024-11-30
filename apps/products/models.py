from optparse import Option

from django.db import models
from apps.utils.models.base_model import AbstractBaseModel


class Product(AbstractBaseModel):
    """ this model creates products """

    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(
        to='categories.Category',
        null=True,
        on_delete=models.SET_NULL,
        related_name='products'
    )
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.PositiveSmallIntegerField(default=0)
    published = models.BooleanField(default=False)
    videos = models.FileField(upload_to='videos/')
    description = models.TextField(max_length=500, blank=True)
    weight = models.PositiveSmallIntegerField(default=0)
    length = models.PositiveSmallIntegerField(default=0)
    brand = models.CharField(max_length=255, blank=True)
    subcategory = models.ForeignKey(
        to='categories.Subcategory',
        null=True,
        on_delete=models.SET_NULL,
        related_name='products'
    )
    product_type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
