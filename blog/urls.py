from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("autor/nuevo/", views.crear_autor, name="crear_autor"),

    path("categoria/nueva/", views.crear_categoria, name="crear_categoria"),

    path("post/nuevo/", views.crear_post, name="crear_post"),

    path("posts/", views.listar_posts, name="listar_posts"),

    path("posts/<int:post_id>/", views.detalle_post, name="detalle_post"),

    path("posts/<int:post_id>/editar/", views.editar_post, name="editar_post"),

    path("posts/<int:post_id>/borrar/", views.borrar_post, name="borrar_post"),

    path("buscar/", views.buscar_post, name="buscar_post"),

    path("accounts/register/", views.register, name="register"),
    
    path("about/", views.about, name="about"),
]
