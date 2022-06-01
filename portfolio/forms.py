from django.forms import ModelForm
from django import forms


from .models import Blog, Apti, Pessoa, Projeto, Cadeira, Linguagem, Curso, Formacao, Tecnologia, Laboratorio, Noticia, \
    Quizz, Comenatario, PadroesUsados, TecnologiaUsada, TrabalhoFinal


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'data': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Select a date','type': 'date'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Titulo'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL link'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Breve descricao'}),
            'feedback': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feedback sobre mim enquanto colega'}),
        }

        labels = {
            'autor': 'Autor',
            'data': 'Data',
            'titulo': 'Título',
            'link': 'Link',
            'descricao': 'Descrição',
        }


class AptiForm(ModelForm):
    class Meta:
        model = Apti
        fields = '__all__'

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

class LinguagemForm(ModelForm):
    class Meta:
        model = Linguagem
        fields = '__all__'

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class FormacaoForm(ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'

class TecnologiaForm(ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'

class LaboratorioForm(ModelForm):
    class Meta:
        model = Laboratorio
        fields = '__all__'

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'

class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

        labels = {
            'questao_1': 'Qual a marca de telemoveis tem uma noticia no site ?',
            'questao_2': 'Quantas tecnologias são faladas ?',
            'questao_3': 'Laravel surgio em que ano ?',
            'questao_4': 'O que quer dizer o príncipio DRY do django ?',
        }

        help_texts = {}

class ComenatarioForm(ModelForm):
    class Meta:
        model = Comenatario
        fields = '__all__'

class PadroesUsadosForm(ModelForm):
    class Meta:
        model = PadroesUsados
        fields = '__all__'

class TecnologiaUsadaForm(ModelForm):
    class Meta:
        model = TecnologiaUsada
        fields = '__all__'

class TrabalhoFinalForm(ModelForm):
    class Meta:
        model = TrabalhoFinal
        fields = '__all__'


