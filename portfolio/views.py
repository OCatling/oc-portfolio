from django.http import Http404
from django.shortcuts import render
from .models import Project, Page
from .forms import ContactForm


def index(request):
    context = {
        'form': ContactForm(),
        'pages': Page.objects.all(),
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
