from django.shortcuts import render, get_object_or_404
from .models import Produto

from django.http import HttpResponse

# Create your views here.
def index(request):
    print(f'Usuário: {request.user}')

    if str(request.user) == 'AnonymousUser':
        usuario = ''
    else:
        usuario = str(request.user.first_name) + ' ' + str(request.user.last_name)

    produtos = Produto.objects.all()

    context = {
        'usuario': usuario,
        'curso': 'Prgramação web com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }

    return render(request, 'produto.html', context)