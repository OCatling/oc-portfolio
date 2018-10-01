from django.shortcuts import render
from .models import Project

# Create your views here.


def index(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'portfolio/index.html', context)
