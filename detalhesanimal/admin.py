from django.contrib import admin
from detalhesanimal.models import cadastro_animais    

# Register your models here.
@admin.register(cadastro_animais)
class cadastro_animaisAdmin(admin.ModelAdmin):
    list_display = ['nome','idade','raca','especie','foto'] 
    search_fields = ['nome','idade','raca','especie']
    list_filter= ['data']
