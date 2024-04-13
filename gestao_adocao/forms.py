from django import forms
from .models import Adotante
from cadastro_animal.models import Animal

class AnimalChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        # Define como o rótulo do item do campo de seleção será exibido
        return obj.nome

class AdotanteForm(forms.ModelForm):
    
    animal_adotado = AnimalChoiceField(queryset=Animal.objects.filter(adotado=False), required=False, label='Nome do animal', widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = Adotante
        fields = ['nome', 'cpf', 'idade', 'telefone', 'email', 'endereco', 'espaco', 'tempo', 'ciente_custos', 'disposicao_fisica_emocional', 'termo_responsabilidade', 'animal_adotado']
        labels = {
            'nome': 'Nome',
            'cpf': 'CPF',
            'idade': 'Idade',
            'telefone': 'Telefone',
            'email': 'Email',
            'endereco': 'Endereço',
            'termo_responsabilidade': 'Aceita o Termo de Responsabilidade acima?',
            'espaco': 'Possui espaço adequado para o animal?',
            'tempo': 'Possui tempo disponível para cuidar do animal?',
            'ciente_custos': 'Está ciente dos custos para manter o animal?',
            'disposicao_fisica_emocional': 'Possui disposição física e emocional para cuidar do animal?',
            'animal_adotado': 'Qual animal deseja adotar?'
        }