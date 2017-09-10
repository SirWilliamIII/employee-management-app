# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('dept_no', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='DeptEmp',
            fields=[
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dept_no', models.ForeignKey(db_column='dept_no', on_delete=django.db.models.deletion.CASCADE, to='capstone.Departments')),
            ],
            options={
                'db_table': 'dept_emp',
            },
        ),
        migrations.CreateModel(
            name='DeptManager',
            fields=[
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dept_no', models.ForeignKey(db_column='dept_no', on_delete=django.db.models.deletion.CASCADE, to='capstone.Departments')),
            ],
            options={
                'db_table': 'dept_manager',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=14)),
                ('last_name', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=1)),
                ('hire_date', models.DateField()),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Salaries',
            fields=[
                ('salary', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='capstone.Employee')),
            ],
            options={
                'db_table': 'salaries',
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='capstone.Employee')),
            ],
            options={
                'db_table': 'titles',
            },
        ),
        migrations.AddField(
            model_name='deptmanager',
            name='emp_no',
            field=models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='capstone.Employee'),
        ),
        migrations.AddField(
            model_name='deptemp',
            name='emp_no',
            field=models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='capstone.Employee'),
        ),
        migrations.AlterUniqueTogether(
            name='salaries',
            unique_together=set([('emp_no', 'from_date')]),
        ),
        migrations.AlterUniqueTogether(
            name='deptmanager',
            unique_together=set([('emp_no', 'dept_no')]),
        ),
        migrations.AlterUniqueTogether(
            name='deptemp',
            unique_together=set([('emp_no', 'dept_no')]),
        ),
    ]
