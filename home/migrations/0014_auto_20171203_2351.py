# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-04 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20171203_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='Mentor_Gender',
            field=models.CharField(help_text='Enter F or M', max_length=10, null=True),
        ),
    ]
