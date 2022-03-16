from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from . import forms

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse('login')
    template_name = 'accounts/signup.html'

