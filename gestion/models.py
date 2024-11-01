# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=150)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.id})"  # Muestra el nombre y el ID del cliente

    class Meta:
        managed = False
        db_table = 'cliente'


class Financiamiento(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, blank=True, null=True)
    monto_financiado = models.DecimalField(max_digits=10, decimal_places=2)
    cuotas = models.IntegerField()
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.cliente} - {self.vehiculo} - ${self.monto_financiado}"

    class Meta:
        managed = False
        db_table = 'financiamiento'


class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateField()
    tipo_servicio = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, blank=True, null=True)
    detalles = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mantenimiento'


class Promocion(models.Model):
    descripcion = models.TextField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, blank=True, null=True)
    
    def __str__(self):
        return f"{self.descripcion} - {self.descuento}%"
    
    class Meta:
        managed = False
        db_table = 'promocion'


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, blank=True, null=True)
    fecha_reserva = models.DateField(blank=True, null=True)
    fecha_prueba = models.DateField(blank=True, null=True)
    hora_prueba = models.TimeField(blank=True, null=True)
    tipo_reserva = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva'


class Transaccion(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'transaccion'


class Usuario(models.Model):
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    especificaciones = models.TextField(blank=True, null=True)
    stock = models.IntegerField()
    estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehiculo'
