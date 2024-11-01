# gestion/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Vehiculo, Reserva, Mantenimiento
from .forms import ReservaForm, FinanciamientoForm, PromocionForm
from django.db.models import Q

# Vista para listar vehículos con funcionalidad de búsqueda
def lista_vehiculos(request):
    query = request.GET.get('q')
    if query:
        vehiculos = Vehiculo.objects.filter(
            Q(marca__icontains=query) | Q(modelo__icontains=query)
        )
    else:
        vehiculos = Vehiculo.objects.all()
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos, 'query': query})

# Vista de detalles de un vehículo específico
def detalle_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    return render(request, 'detalle_vehiculo.html', {'vehiculo': vehiculo})

# Vista para crear una reserva de un vehículo
@login_required
def crear_reserva(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.vehiculo = vehiculo
            reserva.save()
            return redirect('detalle_vehiculo', vehiculo_id=vehiculo.id)
    else:
        form = ReservaForm()
    return render(request, 'crear_reserva.html', {'form': form, 'vehiculo': vehiculo})

# Vista para el historial de reservas (protegida para usuarios autenticados)
@login_required
def historial_reservas(request):
    reservas = Reserva.objects.all()  # Puedes filtrar por cliente si es necesario
    return render(request, 'historial_reservas.html', {'reservas': reservas})

# Vista para el historial de mantenimiento de un vehículo
@login_required
def historial_mantenimiento(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    mantenimientos = Mantenimiento.objects.filter(vehiculo=vehiculo)
    return render(request, 'historial_mantenimiento.html', {'vehiculo': vehiculo, 'mantenimientos': mantenimientos})

@login_required
def crear_financiamiento(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        form = FinanciamientoForm(request.POST)
        if form.is_valid():
            financiamiento = form.save(commit=False)
            financiamiento.vehiculo = vehiculo
            financiamiento.save()
            return redirect('detalle_vehiculo', vehiculo_id=vehiculo.id)
    else:
        form = FinanciamientoForm()
    return render(request, 'crear_financiamiento.html', {'form': form, 'vehiculo': vehiculo})

@login_required
def crear_promocion(request):
    if request.method == 'POST':
        form = PromocionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = PromocionForm()
    return render(request, 'crear_promocion.html', {'form': form})