from django import forms
from django.contrib.auth.models import Group


class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data