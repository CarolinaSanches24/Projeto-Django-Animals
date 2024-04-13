from django.shortcuts import render
from cadastro_animal.models import Animal


def detalhes_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    
    # Renderizar o template com as informações do animal
    return render(request, 'detalhes_animal.html', {'animal': animal})