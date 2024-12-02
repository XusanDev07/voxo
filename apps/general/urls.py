from django.urls import path
from .views import (
    HomeView,
    CreateVendorView,
    VendorsView,
    OrderTrackingView,
    OrderDetailView,
    OrdersView,
    TranslationView,
    CurrencyRateView,
    TaxesView,
    ProductsListView,
    CreateProductView,
    MenusView,
    CreateMenuView,
    CouponsView,
    CreateCouponView,
    ProductReviewView,
    InvoiceView,
    SupportTicketView,
    ProfileSettingsView,
    ReportsView,
    ListPageView,
    LoginView,
    ForgotPasswordView,
    RegisterView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('orders_detail/', OrderDetailView.as_view(), name='order_detail'),
    path('orders_tracking/', OrderTrackingView.as_view(), name='order_tracking'),
    path('vendors/', VendorsView.as_view(), name='vendors'),
    path('add_vendor/', CreateVendorView.as_view(), name='add_vendor'),
    path('translation/', TranslationView.as_view(), name='translation'),
    path('currency_rate/', CurrencyRateView.as_view(), name='currency_rate'),
    path('taxes/', TaxesView.as_view(), name='taxes'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
    path('menus/', MenusView.as_view(), name='menus'),
    path('create_menu/', CreateMenuView.as_view(), name='create_menu'),
    path('coupons/', CouponsView.as_view(), name='coupons'),
    path('create_coupon/', CreateCouponView.as_view(), name='create_coupon'),
    path('product_review/', ProductReviewView.as_view(), name='product_review'),
    path('invoice/', InvoiceView.as_view(), name='invoice'),
    path('support_ticket/', SupportTicketView.as_view(), name='support_ticket'),
    path('profile_settings/', ProfileSettingsView.as_view(), name='profile_setting'),
    path('reports/', ReportsView.as_view(), name='reports'),
    path('list_page/', ListPageView.as_view(), name='list_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('register/', RegisterView.as_view(), name='register'),
]
