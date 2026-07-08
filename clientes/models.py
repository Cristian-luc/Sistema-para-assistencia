from django.db import models

class Clientes(models.Model):
    nome=models.CharField(max_length=50)
    telefone=models.IntegerField
    endereço=models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Aparelho (models.Model):
    modelo=models.CharField(max_length=50)
    fabricante=models.CharField

    def __str__(self):
        return self.modelo
    
class Defeito (models.Model):
    nome_defeito=models.CharField
    preco=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome_defeito



