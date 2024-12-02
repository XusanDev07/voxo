from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('card', 'Card'),
        ('cash', 'Cash'),
        ('paypal', 'PayPal'),
    ]

    img = models.ImageField(upload_to='orders/', blank=True, null=True, verbose_name="Order Image")
    order_code = models.CharField(max_length=20, unique=True, verbose_name="Order Code")
    payment_method = models.CharField(
        max_length=10, choices=PAYMENT_METHOD_CHOICES, default='cash', verbose_name="Payment Method"
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Order Status"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Order Amount")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"Order {self.order_code}"
