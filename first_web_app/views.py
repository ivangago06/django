from django.shortcuts import render,  HttpResponse

# Create your views here.

def home(request):
    return render(request,"first_web_app/home.html")

def about(request):
    return render(request,"first_web_app/about.html")

def portafolio(request):
    return render(request,"first_web_app/portafolio.html")

def contacto(request):
    return render(request,"first_web_app/contacto.html")
