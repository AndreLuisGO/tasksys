# api/models.py
from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class Tarefas(models.Model):
    """Esta classe representa o modelo de Tarefas """
    nome = models.CharField(max_length=255, blank=False, unique=False)
    concluida = models.BooleanField(default=False)


    def __str__(self):
        """Retorna uma representacao compreensivel da instancia do modelo"""
        return"{}".format(self.nome)
