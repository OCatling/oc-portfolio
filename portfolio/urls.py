from django.urls import path, re_path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index),
    re_path(r'^/load_contact_form/$', views.contact_form_request, name='contact_form'),
]
