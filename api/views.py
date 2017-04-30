# api/views.py

from rest_framework import generics
from .serializers import SerializerTarefas
from .models import Tarefas

def common_vars(request):
    return {
        'True': True,
        'False': False,
    }
# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """Esta classe define o comportamento de criar da API REST"""
    queryset = Tarefas.objects.all()
    serializer_class= SerializerTarefas

    def perform_create(self, serializer):
        """Salva os dados do POST quando cria uma nova lista de Tarefas"""
        serializer.save()



class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Esta classe cuida das requisicoes do http GET, PUT e DELETE"""

    queryset = Tarefas.objects.all()
    serializer_class= SerializerTarefas
