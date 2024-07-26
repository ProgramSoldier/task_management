from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
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
                activ_project_id = ProjectModel.objects.get(title=title_project).pk
                if projects:
                    tasks_project = TaskModel.objects.filter(project__title=title_project).select_related("project")
                    context['tasks_project'] = tasks_project
            context['projects'] = projects
            context['title_project'] = title_project
        return render(request, self.template_name, context=context)




    def post(self, request, title_project=None, *args, **kwargs):
        data = request.POST
        print(data)
        #TaskModel.objects.filter(pk=data['task-id']).update(user=request.user)
        #print(TaskModel.objects.get(pk=data['task-id']).user)
        return JsonResponse({1:1}, status=200)


def test(request):
    return JsonResponse({}, status=200)
