from django import forms
from .models import Categoria, Post, Comentario


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "titulo",
            "subtitulo",
            "contenido",
            "categoria",
            "estado",
            "prioridad",
        ]


class BuscarPostForm(forms.Form):
    titulo = forms.CharField(
        max_length=100,
        required=False,
        label="Buscar por título",
        widget=forms.TextInput(
            attrs={"placeholder": "ej: outlook, impresora, vnc, ssd..."}
        ),
    )


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["nombre", "texto"]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Tu nombre"}),
            "texto": forms.Textarea(attrs={"placeholder": "Escribí tu comentario..."}),
        }