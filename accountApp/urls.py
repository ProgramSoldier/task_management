from django.urls import path
from .views import CastomLoginView


urlpatterns = [
    path('', CastomLoginView.as_view(), name='login_account'),
]