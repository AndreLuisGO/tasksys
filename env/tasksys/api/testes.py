#api/testes.py
from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import APIClient
from rest_framework import status
from .models import Tarefas



class ModelTestCase(TestCase):
    """Esta classe define o conjunto de testes para o modelo tarefas"""

    def setUp(self):
        """Define o cliente de teste e outras variaveis de teste"""
        self.tarefas_nome = "Definir nome de tarefas"
        self.tarefas = Tarefas(nome=self.tarefas_nome)

    def modelo_teste_para_criar_tarefas(self):
        """Testa o modelo de tarefas para criar uma lista de tarefas"""
        old_count = Tarefas.objects.count()
        self.tarefas.save()
        new_count = Tarefas.objects.count()
        self.assertNotEqual(old_count, new_count)



Class ViewTestCase(TestCase):
    """Conjunto de testes para as views da API"""

    def setUp(self):
        """Define o cliente de teste e outras variaveis de teste"""
        self.client = APIClient()
        self.dados_tarefa = {'nome': 'Definir metas para equipe'}
        self.response= self.client.post(
            reverse('create'),
            self.dados_tarefa,
            format="json"
        )

    def teste_api_pode_criar_tarefas(self):
        """Testa se a API tem capacidade de criar"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
