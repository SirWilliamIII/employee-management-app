# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0002_auto_20170910_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deptemp',
            old_name='dept_no',
            new_name='department_id',
        ),
        migrations.RenameField(
            model_name='deptemp',
            old_name='emp_no',
            new_name='employee_id',
        ),
        migrations.RenameField(
            model_name='deptmanager',
            old_name='dept_no',
            new_name='department_id',
        ),
        migrations.RenameField(
            model_name='deptmanager',
            old_name='emp_no',
            new_name='employee_id',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='birth_date',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='emp_no',
            new_name='employee_id',
        ),
        migrations.RenameField(
            model_name='titles',
            old_name='emp_no',
            new_name='employee_id',
        ),
        migrations.RemoveField(
            model_name='departments',
            name='dept_name',
        ),
        migrations.RemoveField(
            model_name='departments',
            name='dept_no',
        ),
        migrations.AddField(
            model_name='departments',
            name='department_id',
            field=models.IntegerField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departments',
            name='department_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salaries',
            name='employee_id',
            field=models.ForeignKey(db_column='employee_id', default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='employeeSalaries', to='capstone.Employee'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='deptemp',
            unique_together=set([('employee_id', 'department_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='deptmanager',
            unique_together=set([('employee_id', 'department_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='salaries',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='salaries',
            name='emp_no',
        ),
    ]
