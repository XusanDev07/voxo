from django.urls import path
from .views import CreateGroupView

urlpatterns = [
    path('add/', CreateGroupView.as_view(), name='add_group'),
]
