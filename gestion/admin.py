# gestion/admin.py
from django.contrib import admin
from .models import Vehiculo, Cliente, Reserva, Mantenimiento, Transaccion, Promocion, Financiamiento

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anio', 'precio', 'stock', 'estado')
    search_fields = ('marca', 'modelo')
    list_filter = ('estado',)

admin.site.register(Vehiculo)
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Mantenimiento)
admin.site.register(Transaccion)
admin.site.register(Promocion)
admin.site.register(Financiamiento)
