from django.shortcuts import render, redirect
from .formys import ClienteForm
    
def index(request):
    return render (request, "index.html") 

# Criar
def criar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_clientes")
    else:
        form = ClienteForm()

    return render(request, "clientes.html", {
        "form": form
    })

    


