from django.urls import path, include
from .views import IndexView


handler403 = 'mainApp.views.tr_handler403'
handler404 = 'mainApp.views.tr_handler404'
handler500 = 'mainApp.views.tr_handler500'

urlpatterns = [
    path('', IndexView.as_view(), name='mainPage'),
    path('account/', include('accountApp.urls')),
    path('project/', include('projectsApp.urls'))
]
