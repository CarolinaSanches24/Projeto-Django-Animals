from django.contrib import admin
from cadastro_animal.models import Animal
# Register your models here.
@admin.register(Animal)
class CadastroAdmin(admin.ModelAdmin):
    
    # show fields
    list_display = ['nome','idade','raca','especie','foto'] 
    search_fields = ['nome','idade','raca','especie']
    list_filter= ['data']
