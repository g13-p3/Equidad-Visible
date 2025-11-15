# Contenido del urls.py principal de tu proyecto

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls), 

    # Esto enlaza las URLs de tu aplicación 'test_p' a la raíz del proyecto
    path('', include('test_p.urls')), 
]