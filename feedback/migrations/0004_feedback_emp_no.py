# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20170912_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='emp_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]