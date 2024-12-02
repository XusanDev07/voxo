from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_code', 'status', 'payment_method', 'amount', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('order_code',)
