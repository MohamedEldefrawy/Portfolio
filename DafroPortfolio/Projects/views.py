from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Projects
# Create your views here.
def projects(request) : 
    all_projects = Projects.objects.all()
    context = {'projects':all_projects}
    return render(request , 'Projects/Project.html', context)