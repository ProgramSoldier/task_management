from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import LoginForm


class CastomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'accountApp/Html/login.html'

    def get_success_url(self):
        return reverse_lazy('mainPage')

