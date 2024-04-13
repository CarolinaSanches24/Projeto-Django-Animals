from rest_framework import serializers
from cadastro_animal.models import Animal
import uuid
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
       model = Animal
       exclude = ['id', 'adotado', 'data']
        
     # Sobrescreva o método create para definir o ID automaticamente
    def create(self, validated_data):
        
        # # Definir o novo ID no validated_data usando unicode
        validated_data['id'] = str(uuid.uuid4())
        
        # Chamar o método create da superclasse para criar o objeto
        return super().create(validated_data)