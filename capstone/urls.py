from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^time/', views.current_datetime),
    url(r'^admin/', admin.site.urls),
    url(r'^employees/(?P<pk>[0-9]{6})/profile/$', views.my_profile, name='capstone'),
    url(r'^$', views.index),
]
