from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.manager import Manager

# Create your models here.
class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("CategoriaProd")
        verbose_name_plural = ("CategoriaProds")

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda",null=True,blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.nombre

DNI='DNI'
TIPO_DOCUMENTO = [
    (DNI, 'DNI'),
    ('Carne', 'Carné de Extrangería'),
    ('Pasaporte', 'Pasaporte'),
]
class Cliente(models.Model):
    correo=models.EmailField(max_length=70)
    celular=models.CharField(max_length=15)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    tdocumento=models.CharField(max_length=30,choices=TIPO_DOCUMENTO,default=DNI)
    documento=models.CharField(max_length=10)
    direccion=models.CharField(max_length=100)
    tdatos=models.BooleanField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural = ("Clientes")

    def __str__(self):
        return self.correo


TIPO_COMPROBANTE = [
    ('P', 'PROFORMA'),
    ('B', 'BOLETA'),
    ('F', 'FACTURA'),
]
class Comprobante(models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    tipo=models.CharField(max_length=30,choices=TIPO_COMPROBANTE)
    numero=models.CharField(max_length=10)
    fecha=models.DateField()
    total=models.DecimalField(max_digits=10,decimal_places=2)
    tletras=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = ("Comprobante")
        verbose_name_plural = ("Comprobantes")

    def __str__(self):
        return self.numero

class DetalleComprobante(models.Model):
    comprobante=models.ForeignKey(Comprobante,on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    descripcion=models.CharField(max_length=70)
    punitario=models.DecimalField(max_digits=10,decimal_places=2)
    importe=models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        verbose_name = ("DetalleComprobante")
        verbose_name_plural = ("DetalleComprobantes")

    def __str__(self):
        return self.descripcion
