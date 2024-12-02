from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError


class AddUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'password', 'confirm_password', 'groups')

    def clean(self):
        clean_data = super().clean()
        if clean_data['password'] != clean_data['confirm_password']:
            raise ValidationError({"confirm_password": "passwords do not mat"})
        self.cleaned_data['password'] = make_password(self.cleaned_data['password'])
        return clean_data

    def save(self, commit=True):
        return super().save(commit)

