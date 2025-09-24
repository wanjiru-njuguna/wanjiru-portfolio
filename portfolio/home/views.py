from django.shortcuts import render
from .models import HomePage
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    homecontent = HomePage.objects.first()
    template = loader.get_template('home/home.html')
    context = {"homecontent": homecontent}
    return HttpResponse(template.render(context, request))