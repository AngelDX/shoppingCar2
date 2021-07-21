from django.shortcuts import render
from .models import Producto
# Create your views here.
def index(request):
    objetos=Producto.objects.all()
    return render(request,'core/index.html',{'productos':objetos})