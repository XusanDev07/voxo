from django.contrib.auth.models import Group, ContentType
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.permissions.forms import AddGroupForm


class CreateGroupView(CreateView):
    model = Group
    form_class = AddGroupForm
    success_url = reverse_lazy('home')
    template_name = 'pages/add-new-group.html'
    extra_context = {
        'content_types': ContentType.objects.exclude(
            model__in=['session', 'contenttype', 'group', 'permission', 'logentry']
        ).prefetch_related('permission_set')
    }