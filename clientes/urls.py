from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clientes/", views.criar_cliente, name="clientes"),
]

