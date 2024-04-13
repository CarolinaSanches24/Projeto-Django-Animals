from django.shortcuts import render
from gestao_adocao.forms import AdotanteForm
from cadastro_animal.models import Animal 
from gestao_adocao.models import Adotante



def adocao(request):
    sucesso = False  # Define uma flag de sucesso como falso inicialmente
    form = AdotanteForm(request.POST or None)  # Cria uma instância do formulário AdotanteForm

    if form.is_valid():  # Verifica se o formulário é válido
        sucesso = True  # Se for válido, define a flag de sucesso como verdadeiro
        form.save()  # Salva os dados do formulário

    contexto = {  # Cria um contexto para passar para o template
        'form': form,
        'sucesso': sucesso
    }
    # Obter todos os IDs de animais adotados
    ids_adotados = Adotante.objects.values_list('animal_adotado_id', flat=True)

    # Atualizar os animais adotados no banco de dados de cadastro de animais
    Animal.objects.filter(id__in=ids_adotados).update(adotado=True)
    Animal.objects.exclude(id__in=ids_adotados).update(adotado=False)

    # Retornar uma resposta adequada
    return render(request, 'adocao.html', contexto)  # Renderiza o template adocao.html com o contexto





