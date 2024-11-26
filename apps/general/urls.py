from django.urls import path
from .views import (
    home,
    users,
    add_user,
    orders,
    order_detail,
    order_tracking,
    vendors,
    add_vendor,
)

urlpatterns = [
    path('', home, name='home'),
    path('users/', users, name='users'),
    path('add_user/', add_user, name='add_user'),
    path('orders/', orders, name='orders'),
    path('orders_detail/', order_detail, name='order_detail'),
    path('orders_tracking/', order_tracking, name='order_tracking'),
    path('vendors/', vendors, name='vendors'),
    path('add_vendor/', add_vendor, name='add_vendor'),
]
