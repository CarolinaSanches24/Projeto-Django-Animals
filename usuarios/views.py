from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from cadastro_animal.models import Animal
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import logging
from cadastro_animal.forms import AnimalForm

logger = logging.getLogger(__name__)

# Create your views here.

def cadastroUsers(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('There is already a user with this username')
        
        user = User.objects.create_user(username=username,email=email, password=senha)
        user.save()
        return HttpResponse('user registred sucess!')

def user_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        if user:
            login(request, user)
            return redirect('pagina_apos_login')
        else:
            return render(request, 'erro.html')
        
def pagina_apos_login(request):
    if request.user.is_authenticated:
        animais = Animal.objects.all()
        return render(request, 'pagina_apos_login.html', {'animais': animais})

def logout_view(request):
    logout(request)
    return redirect('user_login') 

def excluir_animal(request, animal_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            animal = get_object_or_404(Animal, pk=animal_id)
            animal.delete()
        return HttpResponseRedirect(reverse('pagina_apos_login')) 
    else:
        return JsonResponse({'erro': 'Método não permitido'}, status=405)

def editar_animal(request, animal_id):
    if request.user.is_authenticated:
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
