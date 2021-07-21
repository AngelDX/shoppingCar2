from django.urls import path
from . import views

app_name="carro"
urlpatterns = [
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),
    path('sumar/<int:producto_id>/', views.sumar_producto, name='sumar'),
    path('limpiar/', views.limpiar_carro, name='limpiar'),
    path('ver_carro/', views.ver_carro, name='ver_carro'),
]