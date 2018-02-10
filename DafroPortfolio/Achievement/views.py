from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Achievement

# Create your views here.
def achievement (request):
    Achievements = Achievement.objects.all()
    context = {'achievements':Achievements}
    return render(request , 'Achievement/Achievement.html', context)