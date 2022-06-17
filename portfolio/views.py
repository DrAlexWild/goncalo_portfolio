from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Blog, Apti, Formacao, Cadeira, Projeto, Tecnologia, Noticia, Laboratorio, Quizz, PadroesUsados, \
    TecnologiaUsada, Comenatario, Trabalho_Final
from .forms import BlogForm, QuizzForm, TecnologiaForm, ComenatarioForm, Trabalho_FinalForm, CadeiraForm, ProjetoForm, \
    NoticiaForm
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
        'Trabalho_Finals': Trabalho_Final.objects.all(),
    }
    return render(request, 'portfolio/Projetos.html', context)

def Contacto_view(request):
    return render(request, 'portfolio/Contacto.html')

def metereologia_view(request):
    return render(request, 'portfolio/metereologia.html')

def covidnews_view(request):
    return render(request, 'portfolio/covidnews.html')

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

@login_required
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


@login_required
def novo_trabalhofinal_view(request):
    if request.method == 'POST':
        form = Trabalho_FinalForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:Projetos'))
    form = Trabalho_FinalForm()
    context = {'form': form}
    return render(request, 'portfolio/novafin.html', context)

@login_required
def edita_trabalhofinal_view(request, trabalhofinal_id):
    post = Trabalho_Final.objects.get(id=trabalhofinal_id)
    if request.method == 'POST':
        form = Trabalho_FinalForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:Projetos'))
    else:
        form = Trabalho_FinalForm(instance=post)
    context = {'form': form, 'trabalhofinal_id': trabalhofinal_id}
    return render(request, 'portfolio/editarfin.html', context)


def apaga_trabalhofinal_view(request, trabalhofinal_id):
    Trabalho_Final.objects.get(id=trabalhofinal_id).delete()
    return HttpResponseRedirect(reverse('portfolio:Projetos'))

@login_required
def novo_cadeira_view(request):
    if request.method == 'POST':
        form = CadeiraForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    form = CadeiraForm()
    context = {'form': form}
    return render(request, 'portfolio/novacad.html', context)

@login_required
def edita_cadeira_view(request, cadeira_id):
    post = Cadeira.objects.get(id=cadeira_id)
    if request.method == 'POST':
        form = CadeiraForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    else:
        form = CadeiraForm(instance=post)
    context = {'form': form, 'cadeira_id': cadeira_id}
    return render(request, 'portfolio/editarcad.html', context)


def apaga_cadeira_view(request, cadeira_id):
    Cadeira.objects.get(id=cadeira_id).delete()
    return HttpResponseRedirect(reverse('portfolio:sobre'))

@login_required
def novo_projeto_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:Projetos'))
    form = ProjetoForm()
    context = {'form': form}
    return render(request, 'portfolio/novapro.html', context)

@login_required
def edita_projeto_view(request, projeto_id):
    post = Projeto.objects.get(id=projeto_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:Projetos'))
    else:
        form = ProjetoForm(instance=post)
    context = {'form': form, 'projeto_id': projeto_id}
    return render(request, 'portfolio/editarpro.html', context)


def apaga_projeto_view(request, projeto_id):
    Projeto.objects.get(id=projeto_id).delete()
    return HttpResponseRedirect(reverse('portfolio:Projetos'))


@login_required
def novo_formacao_view(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    form = FormacaoForm()
    context = {'form': form}
    return render(request, 'portfolio/novaforma.html', context)

@login_required
def edita_formacao_view(request, formacao_id):
    post = Formacao.objects.get(id=formacao_id)
    if request.method == 'POST':
        form = FormacaoForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    else:
        form = FormacaoForm(instance=post)
    context = {'form': form, 'formacao_id': formacao_id}
    return render(request, 'portfolio/editarforma.html', context)


def apaga_formacao_view(request, formacao_id):
    Formacao.objects.get(id=formacao_id).delete()
    return HttpResponseRedirect(reverse('portfolio:sobre'))


@login_required
def novo_noticia_view(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:Web'))
    form = NoticiaForm()
    context = {'form': form}
    return render(request, 'portfolio/novanot.html', context)

@login_required
def edita_noticia_view(request, noticia_id):
    post = Noticia.objects.get(id=noticia_id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:Web'))
    else:
        form = NoticiaForm(instance=post)
    context = {'form': form, 'noticia_id': noticia_id}
    return render(request, 'portfolio/editarnot.html', context)


def apaga_noticia_view(request, noticia_id):
    Noticia.objects.get(id=noticia_id).delete()
    return HttpResponseRedirect(reverse('portfolio:Web'))







































@login_required
def novo_Apti_view(request):
    if request.method == 'POST':
        form = AptiForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    form = AptiForm()
    context = {'form': form}
    return render(request, 'portfolio/novaapti.html', context)

@login_required
def edita_Apti_view(request, apti_id):
    post = Apti.objects.get(id=apti_id)
    if request.method == 'POST':
        form = AptiForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    else:
        form = AptiForm(instance=post)
    context = {'form': form, 'apti_id': apti_id}
    return render(request, 'portfolio/editarapti.html', context)


def apaga_Apti_view(request, apti_id):
    Apti.objects.get(id=apti_id).delete()
    return HttpResponseRedirect(reverse('portfolio:sobre'))
