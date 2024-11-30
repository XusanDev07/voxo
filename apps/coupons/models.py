from apps.categories.models import Category
from apps.products.models import Product
from apps.utils.models.base_model import AbstractBaseModel
from django.db import models


class Coupon(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    code = models.CharField(max_length=100)
    discount = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    quantity = models.IntegerField(default=0)
    discount_type = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title

class Restriction(AbstractBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    minimum = models.IntegerField(default=0)
    maximum = models.IntegerField(default=0)


class Usage(AbstractBaseModel):
    per_limit = models.IntegerField(default=0)
    per_customer = models.IntegerField(default=0)


