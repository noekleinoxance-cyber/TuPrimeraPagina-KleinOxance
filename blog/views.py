from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm, ComentarioForm
from .models import Post

def home(request):
    ultimos = Post.objects.all().order_by("-fecha_publicacion")[:6]
    return render(request, "blog/home.html", {"ultimos": ultimos})

def listar_posts(request):
    posts = Post.objects.all().order_by("-fecha_publicacion")
    return render(request, "blog/listar_posts.html", {"posts": posts})

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AutorForm()
    return render(request, "blog/form.html", {"form": form, "titulo": "Cargar Autor"})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CategoriaForm()
    return render(request, "blog/form.html", {"form": form, "titulo": "Cargar Categoría"})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("detalle_post", post_id=post.id)
    else:
        form = PostForm()
    return render(request, "blog/form.html", {"form": form, "titulo": "Nuevo Post (Solución/Procedimiento)"})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.post = post
            c.save()
            return redirect("detalle_post", post_id=post.id)
    else:
        form = ComentarioForm()

    comentarios = post.comentarios.all().order_by("-fecha")
    return render(request, "blog/detalle_post.html", {"post": post, "form": form, "comentarios": comentarios})

def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("detalle_post", post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/form.html", {"form": form, "titulo": "Editar Post"})

def borrar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect("listar_posts")

    return render(request, "blog/confirm_borrar.html", {"post": post})

def buscar_post(request):
    form = BuscarPostForm(request.GET or None)
    posts = []

    if form.is_valid():
        titulo = form.cleaned_data.get("titulo")
        if titulo:
            posts = Post.objects.filter(titulo__icontains=titulo).order_by("-fecha_publicacion")

    return render(request, "blog/buscar_post.html", {"form": form, "posts": posts})

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})