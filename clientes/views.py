from django.shortcuts import render
from .models import Clientes
    
def listar_clientes(request):
    clientes = Clientes.object.all()

    return render (request, "clientes/lista_clientes.html") 
    {'clientes' : Clientes}


