# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='event',
            field=models.CharField(max_length=30),
        ),
    ]