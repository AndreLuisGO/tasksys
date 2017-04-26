# api/models.py
from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class Tarefas(models.Model):
    """Esta classe representa o modelo de Tarefas """
    nome = models.CharField(max_length=255, blank=False, unique=True)
    data_criada = models.DateTimeField(auto_now_add=True)
    data_modificada = models.DateTimeField(auto_now=True)


    def __str__(self):
        """Retorna uma representacao compreensivel da instancia do modelo"""
        return"{}".format(self.nome)
