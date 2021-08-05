from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('registro_cliente', views.registro_cliente, name='registro_cliente'),
    path('proforma/<slug:pk>/', views.proforma, name='proforma'),
    path('imprimir_proforma/<slug:pk>/', views.imprimir_proforma, name='imprimir_proforma'),
]