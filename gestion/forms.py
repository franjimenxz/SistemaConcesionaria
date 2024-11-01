# gestion/forms.py
from django import forms
from .models import Reserva, Financiamiento, Promocion

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'vehiculo', 'fecha_reserva', 'fecha_prueba', 'hora_prueba']


class FinanciamientoForm(forms.ModelForm):
    class Meta:
        model = Financiamiento
        fields = ['cliente', 'vehiculo', 'monto_financiado', 'cuotas', 'tasa_interes', 'fecha_inicio']
        
class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = ['descripcion', 'descuento', 'fecha_inicio', 'fecha_fin', 'vehiculo']
