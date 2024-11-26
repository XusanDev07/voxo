from django.db import models
from apps.utils.models.base_model import AbstractBaseModel


class Product(AbstractBaseModel):
    """ that models is for list products """

    title = models.CharField(max_length=255)
    description = models.TextField()

    old_price = models.DecimalField(max_digits=5, decimal_places=2, help_text='enter in usd')
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text='enter in usd')
    total_price = models.DecimalField(max_digits=5, decimal_places=2)

    quantity = models.PositiveSmallIntegerField(default=1)

    image = models.ImageField(upload_to='products/image/%Y/%m/%d')

    categories = models.ForeignKey(
        'categories.Category',
        related_name='products',
        on_delete=models.SET_NULL,
        null=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['title']
