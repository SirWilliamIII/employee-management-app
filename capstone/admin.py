from django.contrib import admin
from .models import (Employee, Departments, DeptEmp, DeptManager, Salaries, Titles)

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class MyAdminSite(AdminSite):
    # Text to put at each page's --title
    site_title = ugettext_lazy('HR Buddy')

    # Text to put at top of each page --h1
    site_header = ugettext_lazy('HR Buddy')

    # Text to put at the top of the admin index page
    index_title = ugettext_lazy('HR BUDDY')


my_admin_site = MyAdminSite()


my_admin_site.register(Employee)
my_admin_site.register(Departments)
my_admin_site.register(DeptEmp)
my_admin_site.register(DeptManager)
my_admin_site.register(Salaries)
my_admin_site.register(Titles)
