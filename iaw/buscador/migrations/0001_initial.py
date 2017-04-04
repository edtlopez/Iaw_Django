# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('descripcion', models.URLField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('visitas', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Periodico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.ManyToManyField(to='buscador.Categoria'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='periodico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buscador.Periodico'),
        ),
    ]
