from __future__ import unicode_literals

import os

from django.db import models
from django.db.models import Max
from django.core.files.storage import FileSystemStorage
from stdimage.models import StdImageField


class LocalFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name):
        if os.path.exists(self.path(name)):
            os.remove(self.path(name))
        return name


fs = LocalFileSystemStorage()


class Department(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(unique=True, max_length=40)

    class Meta:
        db_table = 'departments'


def upload_path_handler(self, filename):
    return u'profile/user_{id}/{file}'.format(id=self.pk, file=filename)


class Employee(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    employee_id = models.IntegerField(primary_key=True)
    dob = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hire_date = models.DateField()
    departments = models.ManyToManyField(Department, through='DeptEmp')
    image = StdImageField(upload_to=upload_path_handler, storage=fs, null=True, blank=True,
                          max_length=255, variations={
                            'large': (600, 400),
                            'thumbnail': (100, 100, True),
                            'medium': (300, 200),
                            })

    def __str__(self):
        name = 'first_name=%s, last_name=%s' % (self.first_name, self.last_name)
        return name

    class Meta:
        db_table = 'employees'


class Departments(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'departments'


class DeptEmp(models.Model):
    employee_id = models.ForeignKey('Employee', db_column='emp_no')
    dept_id = models.ForeignKey('Departments', db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'dept_emp'
        unique_together = (('employee_id', 'dept_id'),)


class DeptManager(models.Model):
    dept_id = models.ForeignKey('Departments', db_column='dept_no')
    employee_id = models.ForeignKey('Employee', db_column='emp_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'dept_manager'
        unique_together = ('employee_id', 'dept_id',)


class Salaries(models.Model):
    emp_no = models.ForeignKey(Employee, db_column='emp_no',)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'salaries'


class Titles(models.Model):
    emp_no = models.ForeignKey(Employee, db_column='emp_no',)
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(null=True)

    class Meta:
        db_table = 'titles'
