from django.shortcuts import render, redirect
from django.http import Http404
# Create your views here.
from django.views.generic import CreateView

from post.models import Post
from post.models import Post

from django.shortcuts import render, get_object_or_404
from post.forms import Posts


def crear_post(request):

    return render(request, 'post/crear_post.html')

def eliminar_post(request):

    return render(request, 'post/eliminar_post.html')  #hay que crear esta vista que aun no existe


class PostCreateView(CreateView):

    model = Post
    template_name = 'post/crear_post.html'
    fields = '__all__'


def crear_post2(request):
    context = {}

    # create object of form
    form = Posts(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "post/crear-post-2.html", context)


def listar_post(request):
    posts= Post.published.all()
    return render (request, "post/blog-home.html", {'posteos': posts})


def post_detalle(request, id):
    post = get_object_or_404(Post, id=id, Estado=Post.estado.PUBLISHED)
    return render(request,'post/detalle-post.html',{'post': post})