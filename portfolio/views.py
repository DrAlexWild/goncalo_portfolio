from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Blog, Apti, Formacao, Cadeira, Projeto, Tecnologia, Noticia, Laboratorio, Quizz, PadroesUsados, \
    TecnologiaUsada, Comenatario, TrabalhoFinal_deisi
from .forms import BlogForm, QuizzForm, TecnologiaForm, ComenatarioForm
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
        'TrabalhoFinals': TrabalhoFinal_deisi.objects.all(),
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
        'Comenatarios': Comenatario.objects.all(),
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

def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:Home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')

def view_logout(request):
    logout(request)
    return render(request, 'portfolio/login.html', {
        'message': 'Foi desconetado.'
    })

def nova_tecnologia_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:Web'))
    form = TecnologiaForm()
    context = {'form': form}
    return render(request, 'portfolio/novatec.html', context)


@login_required
def edita_tecnologia_view(request, tecnologia_id):
    post = Tecnologia.objects.get(id=tecnologia_id)
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:Web'))
    else:
        form = TecnologiaForm(instance=post)
    context = {'form': form, 'tecnologia_id': tecnologia_id}
    return render(request, 'portfolio/editartec.html', context)

@login_required
def apaga_tecnologia_view(request, tecnologia_id):
    Tecnologia.objects.get(pk=tecnologia_id).delete()
    return HttpResponseRedirect(reverse('portfolio:Web'))

def novo_comentario_view(request):
    if request.method == 'POST':
        form = ComenatarioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:Web'))
    form = ComenatarioForm()
    context = {'form': form}
    return render(request, 'portfolio/novacom.html', context)

@login_required
def edita_comentario_view(request, comentario_id):
    post = Comenatario.objects.get(id=comentario_id)
    if request.method == 'POST':
        form = ComenatarioForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:Web'))
    else:
        form = ComenatarioForm(instance=post)
    context = {'form': form, 'comentario_id': comentario_id}
    return render(request, 'portfolio/editarcom.html', context)


def apaga_comentario_view(request, comentario_id):
    Comenatario.objects.get(id=comentario_id).delete()
    return HttpResponseRedirect(reverse('portfolio:Web'))

