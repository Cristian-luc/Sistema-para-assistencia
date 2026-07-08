from django.contrib import admin
from .models import Clientes, Aparelho, Defeito

admin.site.register(Clientes)
admin.site.register(Aparelho)
admin.site.register(Defeito)
