from django.urls import path
from .views import CastomLoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', CastomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]