from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.nombre


class Post(models.Model):

    ESTADO_CHOICES = [
        ("abierto", "Abierto"),
        ("en_proceso", "En proceso"),
        ("resuelto", "Resuelto"),
    ]

    PRIORIDAD_CHOICES = [
        ("baja", "Baja"),
        ("media", "Media"),
        ("alta", "Alta"),
        ("critica", "Crítica"),
    ]

    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150, blank=True)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    reportado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default="abierto"
    )

    prioridad = models.CharField(
        max_length=20,
        choices=PRIORIDAD_CHOICES,
        default="media"
    )
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        
    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    nombre = models.CharField(max_length=50)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} -> post {self.post_id}"