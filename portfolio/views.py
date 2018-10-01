from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Project

# Create your views here.


def index(request):
    projects = Project.objects.all()
    template = loader.get_template('portfolio/index.html')
    context = {
        'all_projects': projects
    }
    return HttpResponse(template.render(context, request))
