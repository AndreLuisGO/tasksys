#api/serializers.py

"""Este arquivo utiliza uma classe 'ModelSerializer' para criar
automaticcamente as classes com campos correspondentes do Modelo. """

from rest_framework import serializers
from .models import Tarefas

class SerializerTarefas(serializers.ModelSerializer):
    """Serializar para mapear a instancia do Modelo para formato JSON"""

    class Meta:
        """Classe Meta para mapear  os capmos do serializer com os campos do Modelo"""
        model = Tarefas
        fields = ('id', 'nome', 'data_criada', 'data_modificada')
        read_only_fields =('data_criada', 'data_modificada')
