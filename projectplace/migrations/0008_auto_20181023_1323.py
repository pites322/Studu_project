# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectplace', '0007_auto_20181020_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconnect',
            name='stripe_account',
            field=models.CharField(default='None_imput', max_length=100),
        ),
    ]
