from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class UsersView(TemplateView):
    template_name = 'pages/all-users.html'

class CreateUserView(TemplateView):
    template_name = 'pages/add-new-user.html'

class OrdersView(TemplateView):
    template_name = 'pages/order-list.html'

class OrderDetailView(TemplateView):
    template_name = 'pages/order-detail.html'

class OrderTrackingView(TemplateView):
    template_name = 'pages/order-tracking.html'

class VendorsView(TemplateView):
    template_name = 'pages/vendor-list.html'

class CreateVendorView(TemplateView):
    template_name = 'pages/create-vendor.html'

class TranslationView(TemplateView):
    template_name = 'pages/translation.html'

class CurrencyRateView(TemplateView):
    template_name = 'pages/currency-rates.html'

class TaxesView(TemplateView):
    template_name = 'pages/taxes.html'

class ProductsView(TemplateView):
    template_name = 'pages/products.html'

class CreateProductView(TemplateView):
    template_name = 'pages/add-new-product.html'

class MenusView(TemplateView):
    template_name = 'pages/menu-lists.html'

class CreateMenuView(TemplateView):
    template_name = 'pages/create-menu.html'

class CouponsView(TemplateView):
    template_name = 'pages/coupon-list.html'

class CreateCouponView(TemplateView):
    template_name = 'pages/create-coupon.html'

class ProductReviewView(TemplateView):
    template_name = 'pages/product-review.html'

class InvoiceView(TemplateView):
    template_name = 'pages/invoice.html'

class SupportTicketView(TemplateView):
    template_name = 'pages/support-ticket.html'

class ProfileSettingsView(TemplateView):
    template_name = 'pages/profile-setting.html'

class ReportsView(TemplateView):
    template_name = 'pages/reports.html'

class ListPageView(TemplateView):
    template_name = 'pages/list-page.html'

class LoginView(TemplateView):
    template_name = 'pages/login.html'

class ForgotPasswordView(TemplateView):
    template_name = 'pages/forgot-password.html'

class RegisterView(TemplateView):
    template_name = 'pages/sign-up.html'
