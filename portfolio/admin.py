from django.contrib import admin

# Register your models here.
from .models import Blog, Apti, Pessoa, Projeto, Cadeira, Linguagem, Curso, Formacao, Tecnologia, Laboratorio, Noticia, \
    Quizz, Comenatario, PadroesUsados, TecnologiaUsada

admin.site.register(Blog)
admin.site.register(Apti)
admin.site.register(Pessoa)
admin.site.register(Projeto)
admin.site.register(Cadeira)
admin.site.register(Linguagem)
admin.site.register(Curso)
admin.site.register(Formacao)
admin.site.register(Tecnologia)
admin.site.register(Laboratorio)
admin.site.register(Noticia)
admin.site.register(Quizz)
admin.site.register(Comenatario)
admin.site.register(PadroesUsados)
admin.site.register(TecnologiaUsada)
