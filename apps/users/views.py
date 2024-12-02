from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from apps.users.forms import AddUserForm


# Create your views here.

class UsersView(ListView):
    model = get_user_model()
    template_name = 'pages/all-users.html'
    context_object_name = 'users'

class CreateUserView(CreateView):
    model = get_user_model()
    form_class = AddUserForm
    success_url = reverse_lazy('/')
    template_name = 'pages/add-new-user.html'
