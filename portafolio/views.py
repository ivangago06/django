from django.shortcuts import render
from .models import project

def portafolio(request):
    projects = project.objects.all()
    return render(request, "portafolio/portafolio.html",
                  {'projects':projects})  # <=====
    