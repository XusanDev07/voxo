from django.urls import path
from .views import UsersView, CreateUserView

urlpatterns = [
    path('', UsersView.as_view(), name='users'),
    path('add/', CreateUserView.as_view(), name='add_user'),
]
