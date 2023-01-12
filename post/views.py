from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from post.models import Post
from post.models import Post


def crear_post(request):

    return render(request, 'post/crear_post.html')

def eliminar_post(request):

    return render(request, 'post/eliminar_post.html')  #hay que crear esta vista que aun no existe


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/crear_post.html'
    fields = '__all__'




