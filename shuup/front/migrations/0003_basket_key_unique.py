# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-17 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import shuup.front.models.stored_basket


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_front', '0002_stored_basket_model_name_translatable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedbasket',
            name='key',
            field=models.CharField(db_index=True, default=shuup.front.models.stored_basket.generate_key, max_length=32, unique=True),
        ),
    ]
