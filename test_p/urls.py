# Contenido de test_p/urls.py

from django.urls import path
from . import views 

urlpatterns = [
    # Esto mapea la URL 'test/' a la función 'test' en views.py
    path('test/', views.test, name='test_cuestionario'),
]