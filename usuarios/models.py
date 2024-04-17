from django.db import models

# Create your models here.
class usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50, unique=True)
    cargo_choices = [
        ('voluntário', 'Voluntário'),
        ('cuidador', 'Cuidador'),
        ('admin', 'Admin'),
    ]
    cargo = models.CharField(max_length=15, choices=cargo_choices)
    usuario = models.CharField(max_length=20, unique=True)
    senha = models.CharField(max_length=10)
    
    def __str__(self): 
        return f'{self.nome}, {self.cargo}'
    
    class Meta: # Alterando o nome das bases dentro do admin
        verbose_name = 'Usuarios' # Nome do formulario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nome']