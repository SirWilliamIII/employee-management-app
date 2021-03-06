# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 13:41
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
                ('dept_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='DeptEmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('dept_id', models.ForeignKey(db_column='dept_no', on_delete=django.db.models.deletion.CASCADE, to='capstone.Departments')),
            ],
            options={
                'db_table': 'dept_emp',
            },
        ),
        migrations.CreateModel(
            name='DeptManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('dept_id', models.ForeignKey(db_column='dept_no', on_delete=django.db.models.deletion.CASCADE, to='capstone.Departments')),
            ],
            options={
                'db_table': 'dept_manager',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dob', models.DateField()),
                ('first_name', models.CharField(max_length=14)),
                ('last_name', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('hire_date', models.DateField()),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Salaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='capstone.Employee')),
            ],
            options={
                'db_table': 'salaries',
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='capstone.Employee')),
            ],
            options={
                'db_table': 'titles',
            },
        ),
        migrations.AddField(
            model_name='deptmanager',
            name='employee_id',
            field=models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='capstone.Employee'),
        ),
        migrations.AddField(
            model_name='deptemp',
            name='employee_id',
            field=models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='capstone.Employee'),
        ),
        migrations.AlterUniqueTogether(
            name='deptmanager',
            unique_together=set([('employee_id', 'dept_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='deptemp',
            unique_together=set([('employee_id', 'dept_id')]),
        ),
    ]
