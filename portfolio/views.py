from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    my_projects = Project.objects.all() # .objects.all() se crea en tiempo de ejecuión
    return render(request, 'portfolio/portfolio.html', {'projects': my_projects}) # Diccionario de contexto