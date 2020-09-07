from django.shortcuts import render, render, redirect

def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')