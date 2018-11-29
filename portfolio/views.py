from django.http import Http404
from django.shortcuts import render
from .models import Project
from .forms import ContactForm


def index(request):
    context = {
        'form': ContactForm(),
        'projects': Project.objects.all(),
    }
    return render(request, 'portfolio/index.html', context)


def work(request, slug):
    try:
        work = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404("THIS PAGE DOES NOT EXIST")

    context = {
        'form': ContactForm(),
        'work': work,
    }
    return render(request, 'portfolio/work.html', context)
