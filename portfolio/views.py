from django.shortcuts import render
from django.template import RequestContext
from .models import Project

# Create your views here.


def index(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'portfolio/index.html', context)
