from __future__ import unicode_literals

from django.db import models


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

    def __str__(self):
        name = 'first_name=%s, last_name=%s' % (self.first_name, self.last_name)
        return name

    class Meta:
        db_table = 'employees'


class Departments(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'departments'


class DeptEmp(models.Model):
    employee_id = models.ForeignKey('Employee', db_column='emp_no')
    department_id = models.ForeignKey('Departments', db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'dept_emp'
        unique_together = (('employee_id', 'department_id'),)


class DeptManager(models.Model):
    department_id = models.ForeignKey('Departments', db_column='dept_no')
    employee_id = models.ForeignKey('Employee', db_column='emp_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'dept_manager'
        unique_together = (('employee_id', 'department_id'),)


class Salaries(models.Model):
    employee_id = models.ForeignKey(Employee, db_column='employee_id', related_name='employeeSalaries')
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'salaries'


class Titles(models.Model):
    employee_id = models.ForeignKey(Employee, db_column='emp_no', related_name='employeeTitles')
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'titles'
