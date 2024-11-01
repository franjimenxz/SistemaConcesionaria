"""
URL configuration for concesionaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# concesionaria/urls.py
from django.contrib import admin
from django.urls import path
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('vehiculos/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),  # Nueva ruta para los detalles
    path('vehiculos/<int:vehiculo_id>/reserva/', views.crear_reserva, name='crear_reserva'),
    path('reservas/', views.historial_reservas, name='historial_reservas'),
    path('vehiculos/<int:vehiculo_id>/mantenimiento/', views.historial_mantenimiento, name='historial_mantenimiento'),
    path('vehiculos/<int:vehiculo_id>/financiamiento/', views.crear_financiamiento, name='crear_financiamiento'),
    path('promocion/nueva/', views.crear_promocion, name='crear_promocion'),
]
