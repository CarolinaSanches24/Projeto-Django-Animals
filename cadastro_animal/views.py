import uuid
from django.shortcuts import render
from cadastro_animal.models import Animal
from cadastro_animal.forms import AnimalForm
from rest_framework import viewsets, status
from cadastro_animal.serializers import AnimalSerializer
from django.db.models import Q
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def home(request):
   # Filtrar apenas os animais que não foram adotados
    list_animals = Animal.objects.filter(adotado=False)
  
    return render(request, 'home.html',{'list_animals':list_animals})

def quemsomos(request):
    return render(request, 'quemsomos.html')

def sejaparceiro(request):
    return render(request, 'sejaparceiro.html')


def pesquisa_animal(request):
    query = request.GET.get('q')
    list_animals = Animal.objects.filter(
        Q(nome__icontains=query) | 
        Q(especie__icontains=query) |
        Q(raca__icontains=query)|
        Q(porte__icontains=query)|
        Q(idade__icontains=query)|
        Q(sexo__icontains=query)
       
    ) if query else Animal.objects.filter(adotado=False)
    mensagem = None

    if query and not list_animals:
        mensagem = f"Parametro de busca '{query}' inválido."

    return render(request, 'home.html', {'list_animals': list_animals, 'mensagem': mensagem, 'query': query})

@csrf_protect
def criar_animal(request):
    sucess = False  # Inicialmente, definimos sucesso como falso
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.id = uuid.uuid4()
            animal.save()
            sucess = True  # Definimos sucesso como verdadeiro após salvar com sucesso
            # Limpar o formulário após salvar
            form = AnimalForm()
    else:
        form = AnimalForm()
    
    return render(request, 'cadastro.html', {'form': form, 'sucess': sucess})

    
#! O AnimalSerializer é uma classe que converte objetos Animal em formatos como JSON para serem enviados pela API e vice-versa.
class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_delete(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    
# Com essa configuração,voce consegue fazer as operações CRUD padrão para o modelo Animal . Isso inclui criar, recuperar, atualizar e excluir objetos Animal através da API REST.
