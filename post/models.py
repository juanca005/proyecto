from django.db import models

# Create your models here.
#creacion de los modelos para los post individuales


#defino la clase categoria que estara relacionado con el post individual

class Categoria(models.Model):
    nombre= models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

#defino el modelo de un post en particular
class Post(models.Model):
    #definimos los atributos de la clase
    titulo = models.CharField(max_length=200)
    #imagen_central
    #etiquetas
    fecha_creacion = models.DateTimeField()
    contenido = models.TextField()
    categoria = models.ManyToManyField(Categoria)
    #usuario_creacion
    #estado