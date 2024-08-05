from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', CastomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]