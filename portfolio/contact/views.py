from django.shortcuts import render
from .models import ContactInfo
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def get_contact (request):
    contact_information = ContactInfo.objects.first()
    template = loader.get_template("contact/contact.html")
    context = {"contact_information" :contact_information }
    return HttpResponse(template.render(context, request))
