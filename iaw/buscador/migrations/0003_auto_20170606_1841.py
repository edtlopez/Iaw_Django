# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 18:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0002_auto_20170606_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextension',
            name='user',
        ),
        migrations.DeleteModel(
            name='userextension',
        ),
    ]
