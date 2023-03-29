from django.shortcuts import render

def natal(request):
    contexto = {
        'natal': True
    }
    return render(request, 'natal.html', contexto)

def tiradentes(request):
    contexto = {
        'tiradentes': True
    }
    return render(request, 'tiradentes.html', contexto)