from django.urls import path, include
from .views import *

urlpatterns = [
    path('test/', test, name='test'),
    path('addProject/', ProjectView.as_view(), name='addProject'),
    path('Tasks/', TaskView.as_view(), name='Tasks'),
    path('', ProjectView.as_view(), name='project'),
    #path('<str:title_project>/', ProjectView.as_view(), name='project'),
]
