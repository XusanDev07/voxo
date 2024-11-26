from django.conf import settings
from django.db import models

from apps.utils.models.base_model import AbstractBaseModel


class Purchase(AbstractBaseModel):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Report(AbstractBaseModel):
    title = models.CharField(max_length=55)
    content = models.TextField(max_length=5000)
    author = models.CharField(max_length=55)
    purchase = models.ManyToManyField(Purchase)

class Transfer(AbstractBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transfer_price = models.DecimalField(max_digits=6, decimal_places=2)
    transfer_date = models.DateField()



