from django.shortcuts import render,redirect
from .models import Producto,Comprobante,DetalleComprobante
from .forms import ClienteForm
from shopcar.carro import Carro
from datetime import datetime
from django.db import transaction
from .numero_letras import numero_a_moneda
from .utils import render_to_pdf
from django.http import HttpResponse
# Create your views here.
def index(request):
    objetos=Producto.objects.all()
    return render(request,'core/index.html',{'productos':objetos})

@transaction.atomic
def registro_cliente(request):
    form=ClienteForm(request.POST)
    if form.is_valid():
        post=form.save(commit=False)
        post.save()
        total=float(request.POST.get('total'))
        total_letras=numero_a_moneda(total)
        proforma=Comprobante(cliente=post,tipo="PROFORMA",numero="P000001",fecha=datetime.now(),total=total,tletras=total_letras)
        proforma.save()
        #carro=request.session
        carro=request.session.get("carro")
        for key,value in carro.items():
            detalle=DetalleComprobante(comprobante=proforma ,cantidad=value["cantidad"],descripcion=value["nombre"],punitario=value["precio"],importe=value["subtotal"])
            detalle.save()
        carro=Carro(request)
        carro.limpiar_carro()
        return redirect('proforma', pk=proforma.pk)
    else:
        form=ClienteForm()
    return render(request,'tienda/clie_registro.html',{"form":form})

def proforma(request,pk):
    encabezado=Comprobante.objects.get(id=pk)
    detalle=DetalleComprobante.objects.filter(comprobante_id=encabezado.id)
    
    return render(request,'tienda/proforma.html',{"proforma":encabezado,"productos":detalle})
    
def imprimir_proforma(request,pk):
    encabezado=Comprobante.objects.get(id=pk)
    detalle=DetalleComprobante.objects.filter(comprobante_id=encabezado.id)
    data={
        'proforma':encabezado,
        'productos':detalle
    }
    pdf = render_to_pdf('tienda/proforma_print.html', data)
    return HttpResponse(pdf, content_type='application/pdf')
