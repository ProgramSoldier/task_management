from django.urls import path, include
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='mainPage'),
    path('account/', include('accountApp.urls')),
    path('project/', include('projectsApp.urls'))
]
