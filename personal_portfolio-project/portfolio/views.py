from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.

def home(request):

    projects = Project.objects.all()  # this will grab of database
    return render(request,'portfolio/home.html', {'projects':projects})

def about(request):

    return render(request,'portfolio/about.html')


