# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ponom', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=50)),
                ('ref', models.CharField(max_length=60)),
                ('url', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
