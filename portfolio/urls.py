from django.urls import path
from . import views

app_name = "portfolio"
urlpatterns = [
    path('', views.home_view, name="Home"),
    path("sobre", views.sobre_view, name="Sobre Mim"),
    path("Projetos", views.Projetos_view, name="Projetos"),
    path("Contacto", views.Contacto_view, name="Contacto"),
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

]
