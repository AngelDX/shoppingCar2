from .carro import Carro

def importe_total_carro(request):
    carro=Carro(request)
    total=0
    cantidad=0
    #if request.user.is_authenticated:
    for key, value in request.session["carro"].items():
        total=total+float(value["subtotal"])
        cantidad=cantidad+1
    return {"importe_total_carro":total,"cantidad_productos_carro":cantidad}
    