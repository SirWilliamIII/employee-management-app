from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^employees/(?P<pk>[0-9]{4})/profile/$', views.my_profile, name='capstone')
]
