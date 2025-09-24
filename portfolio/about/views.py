from django.shortcuts import render
from .models import About
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def get_about (request):
    about_items = About.objects.first()
    context = {
    'about_items': about_items
    }
    template = loader.get_template("about/about.html")
    return HttpResponse(template.render(context, request))