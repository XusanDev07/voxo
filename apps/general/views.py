from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def users(request):
    return render(request, 'pages/all-users.html')

def add_user(request):
    return render(request, 'pages/add-new-user.html')

def orders(request):
    return render(request, 'pages/order-list.html')

def order_detail(request):
    return render(request, 'pages/order-detail.html')

def order_tracking(request):
    return render(request, 'pages/order-tracking.html')

def vendors(request):
    return render(request, 'pages/vendor-list.html')

def add_vendor(request):
    return render(request, 'pages/create-vendor.html')

# def home(request):
#     return render(request, 'index.html')
#
# def home(request):
#     return render(request, 'index.html')
#
# def home(request):
#     return render(request, 'index.html')
#
# def home(request):
#     return render(request, 'index.html')
