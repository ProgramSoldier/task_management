from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response

from .models import *


class ProjectView(View):
    template_name = 'projectsApp/Html/project.html'
    def get(self, request, title_project=None, *args, **kwargs):
        context = {}
        if request.user.is_authenticated:
            projects = Project_UserModel.objects.filter(user=request.user).select_related("project")
            if title_project:
                if projects:
                    tasks_project = TaskModel.objects.filter(project__title=title_project).select_related("project", "user").order_by('deadline','title')
                    context['tasks_project'] = tasks_project
                    for i in tasks_project:
                        print(i.dat, i.title)

            context['projects'] = projects
            context['title_project'] = title_project
        return render(request, self.template_name, context=context)

    def post(self, request, title_project=None, *args, **kwargs):
        data = request.POST
        print(data)
        TaskModel.objects.filter(pk=data['task-id']).update(user=request.user)
        return JsonResponse({}, status=200)

def addProject(request):
    if request.POST:
        title = request.POST['title']
        if title:
            project = ProjectModel(title=title)
            project.save()
            user_model = Project_UserModel(project=project, user=request.user, is_author=True)
            user_model.save()
            return JsonResponse({'title': title}, status=200)
        return JsonResponse({'massage': 'Название проекта не может быть пустым'}, status=400)

def test(request):
    context = {
    }
    return render(request, template_name='projectsApp/Html/test.html', context=context)