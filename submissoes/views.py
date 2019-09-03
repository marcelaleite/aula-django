from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Submissao,Autor
from .forms import AutorForm,AutorFormManual, SubmissaoForm

def submissoes_list_view(request):
    obj = Submissao.objects.all()
    contexto = {
        'object': obj
    }
    return render(request,'submissoes/list_view.html',contexto)

def autor_list_view(request):
    obj = Autor.objects.all()
    contexto = {
        'object': obj
    }
    return render(request,'autor/list_view.html',contexto)

def submissoes_detail_view(request,pid):
    # obj = Submissao.objects.get(id=pid)
    obj = get_object_or_404(Submissao,id=pid)
    contexto = {
        'object': obj
    }
    return render(request,'submissoes/detail_view.html',contexto)

def autor_detail_view(request,pid):
    obj = get_object_or_404(Autor,id=pid)
    contexto = {
        'object': obj
    }
    return render(request,'autor/detail_view.html',contexto)

def autor_create_view(request):
    form  = AutorForm(request.POST or None)
    # form = AutorFormManual(request.POST or None)
    if form.is_valid():
        form.save()
        form = AutorForm()
    contexto = {
        'form': form
    }
    return render(request,'autor/create_view.html',contexto)

def autor_update_view(request, pid):
    obj = get_object_or_404(Autor,id=pid)
    form  = AutorForm(request.POST or None,instance=obj)
    # form = AutorFormManual(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
    contexto = {
        'form': form
    }
    return render(request,'autor/create_view.html',contexto)


def submissao_create_view(request):
    form  = SubmissaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SubmissaoForm()
    contexto = {
        'form': form
    }
    return render(request,'submissoes/create_view.html',contexto)