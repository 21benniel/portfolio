from django.shortcuts import render

# Create your views here.

from portfolio_app.models import Resume, Project

def resume_view(request):
    resume = Resume.objects.first()
    return render(request, 'portfolio\\static\\resume.html', {'resume': resume})

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/projects.html', {'projects': projects})

def home(request):
    # resume = Resume.objects.first()
    return render(request, 'portfolio_app/resume.html',content_type='html') 