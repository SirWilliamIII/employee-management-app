from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django import forms
from .models import Employee, Salaries


class EmployeeAdmin(admin.ModelAdmin):

    class Meta:
        model = Employee
        fields = ('employee_id', 'dob', 'first_name', 'last_name', 'gender', 'hire_date')


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salaries
        fields = '__all__'
