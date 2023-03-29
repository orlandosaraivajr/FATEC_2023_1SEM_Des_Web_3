from django.shortcuts import render

def natal(request):
    contexto = {
        'natal': True
    }
    return render(request, 'natal.html', contexto)
