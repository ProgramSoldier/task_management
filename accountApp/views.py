from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import LoginForm


class CastomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'accountApp/Html/login.html'

    def get_success_url(self):
        return reverse_lazy('mainPage')

class RegisterView(View):

    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'accountApp/Html/register.html', context=context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        print(form.non_field_errors)

        context = {
            'form': form
        }
        return render(request, 'accountApp/Html/register.html', context=context)
