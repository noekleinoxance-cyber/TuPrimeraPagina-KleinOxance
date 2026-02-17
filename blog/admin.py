from django.contrib import admin
from .models import Autor, Categoria, Post, Comentario

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Comentario)
