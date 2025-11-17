from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.juegoSelect, name='select'),
    path('global/', views.juegoMundo, name='mundo'),
    path('nacional/', views.juegoChile, name='chile'),
]