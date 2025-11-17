from django.shortcuts import render, redirect

def juegoSelect(request):
    return render(request, 'juego/juego_select.html')

def juegoMundo(request):
    return render(request, 'juego/juego_mundo.html')

def juegoChile(request):
    return render(request, 'juego/juego_chile.html')