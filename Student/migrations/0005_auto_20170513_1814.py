# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_auto_20170328_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='programme',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE')], default='CSE', max_length=3),
        ),
    ]
