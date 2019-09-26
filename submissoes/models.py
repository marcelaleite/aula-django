from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.conf import settings

class Autor(models.Model):
    nome = models.CharField(max_length=120)
    sobrenome = models.CharField(max_length=120)
    email = models.EmailField(max_length=50,null=True, blank=True)
    formacao = models.CharField(max_length=100,null=True,blank=True)
    def get_absolute_url(self):
        return reverse('autor-detail',kwargs={'pid':self.id})
    def __str__(self):
        nome = '[' + self.sobrenome + '] ' + self.nome
        return nome

class Submissao(models.Model):
    titulo = models.CharField(max_length=150)
    resumo = models.TextField()
    data = models.DateField(auto_now_add=True)
    autores = models.ManyToManyField(Autor)
    submetido_por = models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
    aprovado = models.BooleanField(default=False,null=True)
    arquivo = models.FileField(upload_to="submissoes/",null=True, blank=True)

    def get_absolute_url(self):
        # return '{self.id}/'
        return reverse('submissoes:submissoes-detail',kwargs={'pid':self.id})
