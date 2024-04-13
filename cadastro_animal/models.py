from django.db import models
from datetime import datetime


# Create your models here.

class Animal(models.Model):
    id = models.CharField(max_length=10, primary_key=True ,editable=False) 
    nome = models.CharField(max_length=50) 
    idade = models.CharField(max_length=20)
    foto = models.ImageField()
    
    
    especie_choices = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
    ]
    especie = models.CharField(max_length=10, null=True ,choices=especie_choices)
    raca = models.CharField(max_length=20, null=True )
    porte = models.CharField(max_length=10, null=True )
    sexo_choices = [
        ('macho', 'Macho'),
        ('femea', 'Femea'),
    ]
    sexo = models.CharField(max_length=10, choices=sexo_choices, null=True )
    castrado = models.BooleanField(default=False)
    vacinado = models.BooleanField(default=False)
    doencas_existentes = models.TextField(blank=True) #Pode ser deixado em branco
    adotado = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now)
    
    def __str__(self): #Metodo para mostrar detalhes do cadastro dentro do admin
        return f'{self.nome},  {self.foto}, {self.id}'
    
    class Meta: # Alterando o nome das bases dentro do admin
        verbose_name = 'Cadastro de animais' # Nome do formulario'
        # ordering = ['-data'] # Como deve ser ordenado no banco - o hifen é para decrescente 


    
    