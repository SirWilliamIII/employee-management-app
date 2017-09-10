# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=250)),
                ('category', models.CharField(default=b'General', max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('comment', models.CharField(max_length=1000)),
                ('has_read', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]