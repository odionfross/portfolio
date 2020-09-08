from django.shortcuts import render, render, redirect
from .models import *

def index(request):
    context = {
        'all_projects': Project.objects.all()
    }
    print(Project.objects.all()[0].project_main_img)
    return render(request, 'index.html', context)

def project(request, p_id):
    context = {
        'one_project': Project.objects.get(id=p_id),
        'all_projects': Project.objects.all()
    }
    return render(request, 'project.html', context)

def about(request):
    context = {
        'all_projects': Project.objects.all()
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'all_projects': Project.objects.all()
    }
    return render(request, 'contact.html', context)