from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    contexto = {
        'titulo':'Gestão de Feiras',
        'nome':'Marcela Leite',
        'trilhas':['Informática','Agrupecuária', 'Agronomia']
    }
    return render(request,'home.html',contexto)
