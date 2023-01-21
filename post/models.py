from django.db import models
from django.utils import timezone
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(estado=Post.Estado.PUBLISHED)

#creacion de los modelos para los post individuales


#defino la clase categoria que estara relacionado con el post individual

class Categoria(models.Model):
    nombre= models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

#defino el modelo de un post en particular
class Post(models.Model):
    class Estado(models.TextChoices):
        DRAFT = 'DF', 'Borrador'
        PUBLISHED = 'PB', 'Publicado'

    #definimos los atributos de la clase
    titulo = models.CharField(max_length=200)
    #imagen_central
    #etiquetas
    contenido = models.TextField()
    categoria = models.ManyToManyField(Categoria)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    #usuario_creacion
    estado = models.CharField(max_length=2,
                              choices=Estado.choices,
                              default=Estado.DRAFT)

    objects = models.Manager()  # un manejador por defecto de django
    published = PublishedManager()  # mi propio manejador, devuelve todos los post que esten publicados

    class Meta:
        ordering = ['-fecha_publicacion']
        indexes = [
            models.Index(fields=['-fecha_publicacion']),
        ]

    def __str__(self):
        return self.titulo