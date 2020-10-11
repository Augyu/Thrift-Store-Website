from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")


def list(request):
    template = loader.get_template('thrifts/list.html')
    return HttpResponse(template.render())
