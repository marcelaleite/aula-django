from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse
from .models import Submissao,Autor
from .forms import AutorForm,AutorFormManual, SubmissaoForm
from django.views.generic import ListView, DetailView, CreateView

def submissoes_list_view(request):
    obj = Submissao.objects.all()
    contexto = {
        'object': obj
    }
    return render(request,'submissoes/list_view.html',contexto)

class SubmissoesListView(ListView):
    template_name = 'submissoes/class_list.html'
    queryset = Submissao.objects.all() #Submissao_list.html

class SubmissoesDetailView(DetailView):
    template_name = 'submissoes/class_detail.html'
    queryset = Submissao.objects.all() #Submissao_list.html


class SubmissoesCreateView(CreateView):
    template_name = 'submissoes/create_view.html'
    form_class = SubmissaoForm
    queryset = Submissao.objects.all()

    def form_valid(self,form):
        form.instance.submetido_por = self.request.user
        return super().form_valid(form)


class AutorListView(ListView):
    template_name = 'autor/list_view.html'
    queryset = Autor.objects.all()

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

def submissoes_update_view(request, pid):
    obj = get_object_or_404(Submissao,id=pid)
    form  = SubmissaoForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
    contexto = {
        'form': formn
    }
    return render(request,'submissoes/create_view.html',contexto)

def submissao_create_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form  = SubmissaoForm(request.POST, request.FILES or None,initial={'submetido_por': request.user})
            if form.is_valid():
                fn = form.save(commit=False)
                fn.submetido_por = request.user
                fn.save()
        else:
            redirect('../../')
    form = SubmissaoForm()
    contexto = {
        'form': form
    }
    return render(request,'submissoes/create_view.html',contexto)

def submissao_delete_view(request,pid):
    obj = get_object_or_404(Submissao,id=pid)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    contexto = {
        'object': obj
    }
    return render(request,'submissoes/delete_view.html',contexto)
