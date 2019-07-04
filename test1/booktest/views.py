from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View,TemplateView ,ListView
from .models import BookInfo,figureInfo
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("ASDFA")

