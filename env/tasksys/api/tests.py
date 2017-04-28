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

    def test_model_can_create_tarefas(self):
        """Testa o modelo de tarefas para criar uma lista de tarefas"""
        old_count = Tarefas.objects.count()
        self.tarefas.save()
        new_count = Tarefas.objects.count()
        self.assertNotEqual(old_count, new_count)



class ViewTestCase(TestCase):
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

    def test_api_can_create_tarefas(self):
        """Testa se a API tem capacidade CREATE"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def  test_api_can_get_tarefas(self):
        """Testa se a API tem capacidade GET """
        tarefas = Tarefas.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': tarefas.id}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, tarefas)

    def test_api_ca_update_tarefas(self):
        """Testa se a API tem capacidade de UPDATE em uma lista de tarefas"""
        altera_tarefa ={'nome':'Tarefa Nova'}
        res = self.client.put(
            reverse('detalhes', kwargs={'pk': tarefas.id}),
            altera_tarefa, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_tarefas(self):
        """Testa se a API tem capacidade de DELETE em uma lista de tarefas"""
        tarefas = Tarefas.objects.get()
        response = self.client.delete(
            reverse('details', kwargs = {'pk': tarefas.id}),
            format='json',
            follow =True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
