from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ProjectView.as_view(), name='project'),
    path('<str:title_project>/', ProjectView.as_view(), name='project')
]
