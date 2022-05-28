from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Blog, Apti, Formacao, Cadeira, Projeto, Tecnologia, Noticia, Laboratorio, Quizz, PadroesUsados, \
    TecnologiaUsada
from .forms import BlogForm, QuizzForm
from .forms import AptiForm
from .forms import FormacaoForm

# Create your views here.
from .templates.functions import grafico_quiz


def home_view(request):
    return render(request, 'portfolio/home.html')

def sobre_view(request):
    context = {
                  'Formacaos': Formacao.objects.all(),
                  'Aptis': Apti.objects.all(),
                  'Cadeiras': Cadeira.objects.all(),
    }
    return render(request, 'portfolio/sobre.html', context)


def Projetos_view(request):
    context = {
        'Projetos': Projeto.objects.all(),
    }
    return render(request, 'portfolio/Projetos.html', context)

def Contacto_view(request):
    return render(request, 'portfolio/Contacto.html')

def Web_view(request):
    grafico_quiz(Quizz.objects.all())

    form = QuizzForm(request.POST)

    context = {
        'Tecnologias': Tecnologia.objects.all(),
        'Noticias': Noticia.objects.all(),
        'Laboratorios': Laboratorio.objects.all(),
        'PadroesUsadoss': PadroesUsados.objects.all(),
        'TecnologiaUsadas': TecnologiaUsada.objects.all(),
        'form': form,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.path_info)


    return render(request, 'portfolio/Web.html', context)

def Blog_view(request):
    context = {
        'Blogs': Blog.objects.all()
    }
    return render(request, 'portfolio/blogs.html', context)

def nova_view(request):
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('portfolio:Blog'))
        form = BlogForm()
        context = {'form': form}
        return render(request, 'portfolio/nova.html', context)

def edita_Blog_view(request, post_id):
        post = Blog.objects.get(id=post_id)
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('portfolio:Blog'))
        else:
            form = BlogForm(instance=post)
        context = {'form': form, 'post_id': post_id}
        return render(request, 'portfolio/editar.html', context)

def apaga_Blog_view(request, post_id):
    Blog.objects.get(pk=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:Blog'))



def visualizacao_web(request):

    form = QuizzForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse(request.path_info))

    context = {
        'form': form,
    }
    return render(request, 'portfolio/Web.html', context)

