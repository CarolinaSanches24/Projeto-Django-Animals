
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from cadastro_animal.models import Animal
from cadastro_animal.forms import AnimalForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)


# imports login_view
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from funcionarios.models import funcionarios

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         senha = request.POST.get('senha')
#         try:
#             funcionario = funcionarios.objects.get(email=email)
#             usuario = authenticate(request, username=email, password=senha)
#             if usuario is not None:
#                 login(request, usuario)
#                 return redirect('pagina_apos_login')
#             else:
#                 messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
#         except funcionarios.DoesNotExist:
#             messages.error(request, 'Email não encontrado. Por favor, tente novamente.')
#     return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # Verificar se os campos de email e senha estão preenchidos
        if email and senha:
            try:
                funcionario = funcionarios.objects.get(email=email)
                usuario = authenticate(request, username=email, password=senha)
                if usuario is not None:
                    login(request, usuario)
                    return redirect('pagina_apos_login')
                else:
                    messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
            except funcionarios.DoesNotExist:
                messages.error(request, 'Email não encontrado. Por favor, tente novamente.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

    return render(request, 'login.html')

        
def pagina_apos_login(request):
    animais = Animal.objects.all()
    return render(request, 'pagina_apos_login.html', {'animais': animais})

def logout_view(request):
    logout(request)
    return redirect('login') 

def excluir_animal(request, animal_id):
    if request.method == 'POST':
        animal = get_object_or_404(Animal, pk=animal_id)
        animal.delete()
        return HttpResponseRedirect(reverse('pagina_apos_login')) 
    else:
        return JsonResponse({'erro': 'Método não permitido'}, status=405)


def editar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            logger.info('Formulário válido. Salvando alterações.')
            return redirect('pagina_apos_login')
        else:
            logger.error('Formulário inválido: %s', form.errors)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'editar_animal.html', {'form': form})


