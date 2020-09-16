from django.shortcuts import render, render, redirect
from .models import *

def index(request):
    context = {
        'all_projects': Project.objects.all()
    }
    print(Project.objects.all()[0].project_main_img)
    return render(request, 'index.html', context)

def project(request, id):
    context = {
        'one_project': Project.objects.get(id=id),
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
    # if a user submits the form
    if request.method == 'POST':
        print(f"Entering post {request.POST}")
        return redirect('/contact')
    
    return render(request, 'contact.html', context)

def admin(request):
    context = {
        'all_projects': Project.objects.all()
    }
    print(f"Entering get {request.GET}")
    # if user enters the secret key correctly
    key = 'CodingDojo'
    if request.method == 'POST':
        print(f"Entering post {request.POST}")
        if key == request.POST['secret_key']:
            request.session['user_id'] = 1
            return redirect('/')
        return redirect('/admin')
    return render(request, 'admin.html', context)

def add_project(request):
    if request.method == 'POST':
        Project.objects.create(
            project_name = request.POST['project_name'],
            project_main_img = request.POST['project_main_img'],
            short_desc = request.POST['short_desc'],
            role_heading = request.POST['role_heading'],
            role_desc = request.POST['role_desc'],
            background_heading = request.POST['background_heading'],
            background_desc = request.POST['background_desc'],
            problem_heading = request.POST['problem_heading'],
            problem_desc = request.POST['problem_desc'],
            challenges_heading = request.POST['challenges_heading'],
            challenges_desc = request.POST['challenges_desc'],
            user_research_heading = request.POST['user_research_heading'],
            user_research_img1 = request.POST['user_research_img1'],
            user_research_img2 = request.POST['user_research_img2'],
            user_research_desc = request.POST['user_research_desc'],
            solution_heading = request.POST['solution_heading'],
            solution_img = request.POST['solution_img'],
            solution_desc1 = request.POST['solution_desc1'],
            solution_desc2 = request.POST['solution_desc2'],
            key_screen_heading = request.POST['key_screen_heading'],
            key_screen_img1 = request.POST['key_screen_img1'],
            key_screen_img2 = request.POST['key_screen_img2'],
            key_screen_img3 = request.POST['key_screen_img3'],
            key_screen_img4 = request.POST['key_screen_img4'],
            key_screen_img5 = request.POST['key_screen_img5'],
            key_screen_img6 = request.POST['key_screen_img6'],
            key_screen_img7 = request.POST['key_screen_img7'],
            key_screen_img8 = request.POST['key_screen_img8'],
            key_screen_img9 = request.POST['key_screen_img9'],
            learned_heading = request.POST['learned_heading'],
            learned_desc = request.POST['learned_desc'],
            results_heading = request.POST['results_heading'],
            results_desc = request.POST['results_desc'],
            results_data = request.POST['results_data'])
        return redirect('/')
    return render(request, 'new_project.html')

def edit_project(request, id):
    # if get request, then display the forms for the edit
    context = {
        'one_project': Project.objects.get(id=id)
    }

    # store the updated user instance in the database
    if request.method == 'POST':
        print("Entering post request in edit project")
        one_project = Project.objects.get(id=id)
        one_project.project_name = request.POST['project_name']
        one_project.project_main_img = request.POST['project_main_img']
        one_project.short_desc = request.POST['short_desc']
        one_project.role_heading = request.POST['role_heading']
        one_project.role_desc = request.POST['role_desc']
        one_project.background_heading = request.POST['background_heading']
        one_project.background_desc = request.POST['background_desc']
        one_project.problem_heading = request.POST['problem_heading']
        one_project.problem_desc = request.POST['problem_desc']
        one_project.challenges_heading = request.POST['challenges_heading']
        one_project.challenges_desc = request.POST['challenges_desc']
        one_project.user_research_heading = request.POST['user_research_heading']
        one_project.user_research_img1 = request.POST['user_research_img1']
        one_project.user_research_img2 = request.POST['user_research_img2']
        one_project.user_research_desc = request.POST['user_research_desc']
        one_project.solution_heading = request.POST['solution_heading']
        one_project.solution_img = request.POST['solution_img']
        one_project.solution_desc1 = request.POST['solution_desc1']
        one_project.solution_desc2 = request.POST['solution_desc2']
        one_project.key_screen_heading = request.POST['key_screen_heading']
        one_project.key_screen_img1 = request.POST['key_screen_img1']
        one_project.key_screen_img2 = request.POST['key_screen_img2']
        one_project.key_screen_img3 = request.POST['key_screen_img3']
        one_project.key_screen_img4 = request.POST['key_screen_img4']
        one_project.key_screen_img5 = request.POST['key_screen_img5']
        one_project.key_screen_img6 = request.POST['key_screen_img6']
        one_project.key_screen_img7 = request.POST['key_screen_img7']
        one_project.key_screen_img8 = request.POST['key_screen_img8']
        one_project.key_screen_img9 = request.POST['key_screen_img9']
        one_project.learned_heading = request.POST['learned_heading']
        one_project.learned_desc = request.POST['learned_desc']
        one_project.results_heading = request.POST['results_heading']
        one_project.results_desc = request.POST['results_desc']
        one_project.results_data = request.POST['results_data']
        one_project.save()
        return redirect(f'/project/{id}')
    return render (request, "edit_project.html", context)

def delete_project(request, id):
    Project.objects.get(id=id).delete()
    return redirect('/')

def log_out(request):
    request.session.clear()
    return redirect('/')