from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#request como argumento es una peticion de servidor de django
def bienvenido(request):
    #el return permite devolver un resultado a la pagina
    #creamos un diccionario con un valor fijo para mostrar en la vista
    creador = {
        'username' : 'Juan Fresco'
    }
    #agregamos creador , o sea el diccionario que queremos enviar a la vista
    #return render(request, 'blog/index.html', creador) #CON ESTO MANEJAMOS A UNA CARPETA QUE CONTIENE LA TECNOLOGIA FRONT


    return render(request, 'blog/index.html')
    #return HttpResponse('hola mundo')  #CON ESTO SOLO MUETRO UN MJS PLANO


def about(request):

    return render(request, 'blog/about.html')


def blog_home(request):

    return render(request, 'blog/blog-home.html')

def single_post(request):

    return render(request, 'blog/blog-post.html')


