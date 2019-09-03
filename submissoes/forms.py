from django import forms
from .models import Autor,Submissao

class AutorForm(forms.ModelForm):
    formacao = forms.CharField(label='Formação Acadêmica',required=False, widget=forms.Textarea(attrs={'placeholder':'Informe sua formação acadêmica...','id':'formacao','class':'campos','rows':5}))
    class Meta:
         model = Autor
         fields = [
         'nome',
         'sobrenome',
         'email',
         'formacao'
         ]
    def clean_nome(self, *args, **kwargs):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError('O campo nome não está preenchido corretamente')
        return nome

class AutorFormManual(forms.Form):
    nome = forms.CharField(max_length='120')
    sobrenome = forms.CharField(max_length='120')

    def clean_nome(self, *args, **kwargs):
        nome = self.cleaned_data.get('nome')
        if not 'de' in nome:
            raise forms.ValidationError('Nome não compatível com o padrão')
        return nome

class SubmissaoForm(forms.ModelForm):
    class Meta:
        model = Submissao
        fields = [
        'titulo',
        'resumo',
        'autores',
        'aprovado',
        'submetido_por',
        'arquivo'
        ]
