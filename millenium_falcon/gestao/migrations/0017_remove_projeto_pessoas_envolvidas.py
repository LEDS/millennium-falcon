# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 18:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0016_auto_20170517_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='pessoas_envolvidas',
        ),
    ]