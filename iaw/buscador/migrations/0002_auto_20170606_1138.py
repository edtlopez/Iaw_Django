# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='author',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='titulo',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='userextension',
            name='pregunta_secreta',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='userextension',
            name='respueste_secreta',
            field=models.CharField(max_length=1000),
        ),
    ]