from django.urls import path
from . import views

app_name = "portfolio"
urlpatterns = [
    path('', views.home_view, name="Home"),
    path("sobre", views.sobre_view, name="Sobre Mim"),
    path("Projetos", views.Projetos_view, name="Projetos"),
    path("Contacto", views.Contacto_view, name="Contacto"),
    path("metereologia", views.metereologia_view, name="metereologia"),
    path("Web", views.Web_view, name="Web"),
    path("Blog", views.Blog_view, name="Blog"),
    path("nova", views.nova_view, name="nova"),
    path('editar/<int:post_id>', views.edita_Blog_view, name='editar'),
    path('apaga/<int:post_id>', views.apaga_Blog_view, name='apagar'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout'),
    path("tecnologia_nova", views.nova_tecnologia_view, name="tecnologia_nova"),
    path('tecnologia_editar/<int:tecnologia_id>', views.edita_tecnologia_view, name='tecnologia_editar'),
    path('tecnologia_apaga/<int:tecnologia_id>', views.apaga_tecnologia_view, name='tecnologia_apagar'),
    path('comentario_novo/', views.novo_comentario_view, name='comentario_novo'),
    path('comentario_edita/<int:comentario_id>', views.edita_comentario_view,name='comentario_edita'),
    path('comentario_apaga/<int:comentario_id>', views.apaga_comentario_view,name='comentario_apaga'),
    path('trabalhofinal_novo/', views.novo_trabalhofinal_view, name='trabalhofinal_novo'),
    path('trabalhofinal_edita/<int:trabalhofinal_id>', views.edita_trabalhofinal_view, name='trabalhofinal_edita'),
    path('trabalhofinal_apaga/<int:trabalhofinal_id>', views.apaga_trabalhofinal_view, name='trabalhofinal_apaga'),

]
