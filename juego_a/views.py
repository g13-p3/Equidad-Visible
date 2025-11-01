from django.shortcuts import render
from django.http import HttpResponse

def juego(request):
    return render(request, 'juego/juego.html')
