from django.shortcuts import render
from .models import Project
from .forms import ContactForm


def index(request):
    context = {
        'form': ContactForm(),
        'projects': Project.objects.all(),
    }
    return render(request, 'portfolio/index.html', context)


def contact_form_request(request):
    context = {
        'form': ContactForm(),
    }
    return render(request, 'portfolio/contact.html', context)