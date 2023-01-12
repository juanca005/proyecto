"""CoderProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from webapp.views import bienvenido, about,blog_home,single_post  # importo la nueva funcion y agrego las urlpatterns
from post.views import crear_post
urlpatterns = [
    path('admin/', admin.site.urls),  #ruta para acceder al admin de django
    path('', bienvenido),  #dejo solo comillas para indicar que es la vista que tomara como inicio el proyecto
    path('blog/about/', about), #ruta acerca de......
    path('blog/blog_home/', blog_home),  #ruta del home de los post
    path('blog/blog_home/single_post/', single_post),   #ruta para visualizar un post individual
    path('/blog/blog_home/single_post/', single_post),  # ruta para visualizar un post individual
    path('', include('post.urls')),
    # path('index/', bienvenido), # este path es para apuntar la vista de bienvenido
]
