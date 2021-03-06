# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 03:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_feedback_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='category',
            field=models.CharField(choices=[('1', 'General'), ('2', 'Management'), ('3', 'Compensation'), ('4', 'Suggestions'), ('5', 'Complaint')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(max_length=150, validators=[django.core.validators.EmailValidator(), django.core.validators.MinLengthValidator(7)]),
        ),
    ]
