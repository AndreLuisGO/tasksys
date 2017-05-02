# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('concluida', models.CharField(max_length=255, unique=False, default="Nao")),
            ],
        ),
    ]
