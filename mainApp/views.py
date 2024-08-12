from django.shortcuts import render
from django.views.generic import View

class IndexView(View):
    template_name = 'mainApp/Html/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def tr_handler404(request, exception):
    """
    Обработка ошибки 404
    """
    return render(request, 'mainApp/HTML/error.html', status=404, context={
        'title': 'Страница не найдена: 404',
        'message': 'К сожалению такая страница была не найдена, или перемещена',
    })


def tr_handler500(request):
    """
    Обработка ошибки 500
    """
    return render(request, 'mainApp/HTML/error.html', status=500, context={
        'title': 'Ошибка сервера: 500',
        'error_message': 'Внутренняя ошибка сайта, вернитесь на главную страницу, отчет об ошибке мы направим администрации сайта',
    })


def tr_handler403(request, exception):
    """
    Обработка ошибки 403
    """
    return render(request, 'mainApp/HTML/error.html', status=403, context={
        'title': 'Ошибка доступа: 403',
        'error_message': 'Доступ к этой странице ограничен',
    })







