# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_defaultia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeitem',
            name='name',
            field=models.TextField(),
        ),
    ]