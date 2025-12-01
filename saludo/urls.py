"""
URL configuration for saludo project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Esta línea permite entrar usando /home/
    path('home/', include('mensaje.urls')), 

    # Esta línea permite entrar a la página principal sin escribir nada (recomendado dejarla)
    path('', include('mensaje.urls')),
]