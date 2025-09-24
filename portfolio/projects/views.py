from django.shortcuts import render
from .models import ProjectList
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def get_projects (request):
    projects_done = ProjectList.objects.all()
    template = loader.get_template("projects/projects.html")
    context = {"projects_done" : projects_done}
    return HttpResponse (template.render(context, request) )
