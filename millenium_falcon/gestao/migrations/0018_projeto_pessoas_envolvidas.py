# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0010_auto_20170517_1909'),
        ('gestao', '0017_remove_projeto_pessoas_envolvidas'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='pessoas_envolvidas',
            field=models.ManyToManyField(blank=True, to='pessoas.Pessoa'),
        ),
    ]
