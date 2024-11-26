from django.db import models
from django.conf import settings


from django.utils.timezone import now
from apps.utils.models.base_model import AbstractBaseModel


class Orders(AbstractBaseModel):
    """ This model is used to store orders """

    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="orders/image/%Y/%m/%d/")
    payment_method = models.ForeignKey('general.PaymentMethod', on_delete=models.PROTECT)
    deliver_status = models.CharField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=10, unique=True)
    is_paid = models.BooleanField(default=False, editable=False)
    paid_at = models.DateTimeField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if self.is_paid and self.paid_at:
            self.paid_at = now()
        super().save(*args, **kwargs)

class TrackingProcess(AbstractBaseModel):
    """ This model is used to track the order statuses and their timestamps """

    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.status



class Tracking(AbstractBaseModel):
    """
    This model is used to track the status history of the orders
    and it connected with users then them can check and look
    """
    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    process = models.ForeignKey(TrackingProcess, on_delete=models.SET_NULL, null=True, blank=True)