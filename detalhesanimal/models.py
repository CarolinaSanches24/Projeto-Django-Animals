from django.db import models

class cadastro_animais(models.Model):
    id = models.CharField(max_length=10, primary_key=True) #Vinculado ao chip do animal
    nome = models.CharField(max_length=50) 
    idade = models.IntegerField()
    
    
    especie_choices = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
    ]
    especie = models.CharField(max_length=10, choices=especie_choices)
    raca = models.CharField(max_length=20)
    porte = models.CharField(max_length=10)
    sexo_choices = [
        ('macho', 'Macho'),
        ('femea', 'Fêmea'),
    ]
    sexo = models.CharField(max_length=10, choices=sexo_choices)
    castrado = models.BooleanField(default=False)
    vacinado = models.BooleanField(default=False)
    doencas_existentes = models.TextField(blank=True) #Pode ser deixado em branco
    adotado = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='animal_photos/', blank=True)
    
    def __str__(self): #Metodo para mostrar detalhes do cadastro dentro do admin
        return f'{self.nome}, {self.raca}, {self.especie}, {self.adotado}'
    
    class Meta: # Alterando o nome das bases dentro do admin
        verbose_name = 'Cadastro de animais' # Nome do formulario'
        ordering = ['-data'] # Como deve ser ordenado no banco - o hifen é para decrescente 
