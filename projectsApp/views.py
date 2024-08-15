from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response

from .models import *


class ProjectView(View):
    template_name = 'projectsApp/Html/project.html'

    def get(self, request, *args, **kwargs):
        """
        Функция возвращает основную страницу проектов
        """
        context = {}
        project_id = request.GET.get('project_id', 0)  # Получение id проекта
        if request.user.is_authenticated:
            # Получение проектов пользователя
            projects = Project_UserModel.objects.filter(user=request.user).select_related('project').order_by(
                'project_id')
            if project_id:
                if projects:
                    # Обработка запроса к недоступному проекту
                    if not projects.filter(project_id=project_id):
                        return render(request, 'mainApp/Html/error.html', status=404,
                                      context={'title': 'Проект не найден',
                                               'message': 'Данный проект не найден'})
                    # Получение пользователей, которые состоят в проекте
                    users = Project_UserModel.objects.values('user__username').filter(project_id=project_id)
                    # Получение задач проекта с сортировкой по дедлайну и названию задачи
                    tasks_project = TaskModel.objects.filter(project_id=project_id).select_related('user', 'project').order_by(
                        'deadline', 'title')
                    context['tasks_project'] = tasks_project
                    context['project_id'] = project_id
                    context['users'] = users
            context['projects'] = projects
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        """
        Функция добавляет новый проект
        """
        if request.POST:
            title = request.POST['title_project']
            if title:
                project = ProjectModel(title=title)
                project.save()
                user_model = Project_UserModel(project=project, user=request.user, is_author=True)
                user_model.save()
                return JsonResponse({'title': title}, status=200)
            return JsonResponse({'massage': 'Название проекта не может быть пустым'}, status=400)


class TaskView(View):
    def post(self, request):
        do = request.POST['do']

        # Обновление исполнителя задачи
        if do == 'update_task_user':
            data = request.POST
            # print(data)
            TaskModel.objects.filter(pk=data['task-id']).update(user=request.user)
            return JsonResponse({'user': request.user.username, 'task_id': data['task-id']}, status=200)

        # Создание новой задачи
        elif do == "create_task":
            title = request.POST['title_task']
            deadline = request.POST['deadline']
            comment = request.POST.get('comment', None)
            project_id = request.POST['project_id']
            if title and deadline:
                newTask = TaskModel(title=title, deadline=deadline, comment=comment, project_id=int(project_id))
                newTask.save()
                context = {
                    'title': title,
                    'deadline': deadline,
                    'comment': comment,
                    'task_id': newTask.pk,
                }
                return JsonResponse(context, status=200)
            return JsonResponse({'massage': 'Название проекта не может быть пустым'}, status=400)

        # Обновление статуса задачи
        elif do == 'update_is_ready':
            task_id = request.POST['task-id']
            TaskModel.objects.filter(pk=task_id).update(is_ready=True)
            return JsonResponse({'task_id': int(task_id)}, status=200)
        else:
            return JsonResponse({'massage': 'Что-то пошло не так'}, status=404)


def addUserProject(request):
    """
    Функция добавляет нового пользователя в проект
    """
    if request.method == 'POST':
        data = request.POST
        try:
            user = User.objects.get(username=data['username'])
            check_user_in_project = Project_UserModel.objects.filter(user=user, project_id=data['project_id'])
            # Проверка наличия пользователя в проекте
            if check_user_in_project:
                return JsonResponse({'message': 'Пользователь уже состоит в проекте'}, status=400)
            # Добавление пользователя в проект
            new_user_in_project = Project_UserModel(user=user, project_id=data['project_id'])
            new_user_in_project.save()
            return JsonResponse({'username': data['username']}, status=200)
        # Обработка ошибки ненахождения пользователя в системе
        except User.DoesNotExist:
            return JsonResponse({'message': 'Пользователь не найден'}, status=404)
        # Обработка непредвиденных ошибок
        except:
            return JsonResponse({'message': 'Что-то пошло не так. Попробуйте позже'}, status=404)
    # Обработка get запроса
    return render(request, 'mainApp/Html/error.html', status=404, context={'title': '404',
                                                                           'message': 'Страница не найдена.'})


# Функция для тестирования
def test(request):
    context = {
    }
    return render(request, template_name='projectsApp/Html/test.html', context=context)
