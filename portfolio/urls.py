from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    # Home /
    path('', views.index, name="home"),

    # Portfolio Post /Post/
    path('<slug:slug>/', views.work, name="work")
]
