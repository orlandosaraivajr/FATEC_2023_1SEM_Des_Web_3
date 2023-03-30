from django.shortcuts import render

def tela1(request):
    return render(request, 'index.html')
