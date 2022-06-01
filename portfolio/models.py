from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Blog(models.Model):
    autor = models.CharField(max_length = 30)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length = 50)
    descricao = models.TextField()
    link = models.URLField(max_length=200)
    imagem = models.ImageField(default="default.png",blank=True,upload_to='blogeiros/')
    feedbackColega = models.CharField(max_length = 200, default="")

    def yearpublished(self):
        return self.data.strftime('%Y')

    def __str__(self):
        return self.titulo[:40]


class Apti(models.Model):
    titulo = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 200)
    projetos = models.CharField(max_length=100)
    disciplinas = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo[:40]

class Pessoa(models.Model):
        nome = models.CharField(max_length=50, default="")
        linkLusofona = models.CharField(max_length=200, default="",blank=True)
        linkLinkedin = models.CharField(max_length=200, default="",blank=True)
        linkPortfolio = models.CharField(max_length=200, blank=True)
        tipo = models.CharField(max_length=50, default="",blank=True)

        def __str__(self):
            return self.nome[:50]


class Tecnologia(models.Model):
    nome = models.CharField(max_length=200)
    acronimo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50,default="")
    ano_criacao = models.CharField(max_length=50)
    criador = models.ManyToManyField(Pessoa)
    logotipo = models.ImageField(default="default.png",blank=True)
    link_site_oficial = models.URLField(max_length=200)
    descricao_caracteristicas = models.TextField()

    def __str__(self):
        return self.nome[:40]


class Projeto(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    ano = models.CharField(max_length=30, default="")
    linkCadeira = models.URLField(max_length=200)
    linkGitHub = models.URLField(max_length=200, blank=True)
    linkYoutube = models.URLField(max_length=200, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia)
    competencias = models.ManyToManyField(Apti)
    paticipantes = models.ManyToManyField(Pessoa)


    def __str__(self):
            return self.titulo[:40]


class Linguagem(models.Model):
        nome = models.CharField(max_length=50)
        nivel = models.CharField(max_length=50)

        def __str__(self):
            return self.nome[:40]

class Curso(models.Model):
        nome = models.CharField(max_length=50)
        alunos = models.ManyToManyField(Pessoa,blank=True)

        def __str__(self):
            return self.nome[:40]

class Cadeira(models.Model):
    nome = models.CharField(max_length=50,default="")
    ano = models.CharField(max_length=20,default="")
    semestre = models.CharField(max_length=20,default="")
    ects = models.IntegerField(null=True)
    descricao = models.TextField()
    docente_teorica = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    docentes_praticas = models.ManyToManyField(Pessoa, related_name='praticas')
    projetos = models.ManyToManyField(Projeto,blank=True)
    linguagens = models.ManyToManyField(Linguagem,blank=True)
    curso = models.ManyToManyField(Curso)
    imagem = models.ImageField(default="default.png",blank=True)
    linkCadeira = models.URLField(max_length=200,blank=True)
    ranking = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.nome[:40]

class Formacao(models.Model):
    ensino = models.CharField(max_length=50)
    curso = models.CharField(max_length=50,default="")
    periodo = models.IntegerField()
    local = models.CharField(max_length=150)
    logotipo = models.ImageField(default="default.png",blank=True)

    def __str__(self):
        return self.ensino[:40]

class Laboratorio(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    link = models.URLField(max_length=200)
    imagem = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.titulo[:40]

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    link = models.URLField(max_length=200)
    imagem = models.ImageField(default="default.png",blank=True)


    def __str__(self):
        return self.titulo[:40]

class TrabalhoFinal(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ManyToManyField(Pessoa,related_name='autor')
    orientador = models.ManyToManyField(Pessoa,related_name='orientador')
    ano = models.IntegerField()
    descricao = models.TextField()
    resumo = models.CharField(max_length=500)
    linkrelatorio = models.URLField(max_length=200,blank=True)
    linkgithub = models.URLField(max_length=200,blank=True)
    linkYoutube = models.URLField(max_length=200,blank=True)
    imagem = models.ImageField(default="default.png", blank=True)


class Quizz(models.Model):
    questao_1 = models.CharField(max_length=30)
    questao_2 = models.IntegerField(default=0)
    questao_3 = models.IntegerField(default=0)
    questao_4 = models.CharField(max_length=70)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome[:50]

class TecnologiaUsada(models.Model):
    usadas = models.ManyToManyField(Tecnologia)

class PadroesUsados(models.Model):
    nome = models.CharField(max_length=50)

class Comenatario(models.Model):
    sobre = models.CharField(max_length=50)
    texto = models.TextField()










