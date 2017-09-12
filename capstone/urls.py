from django.conf.urls import url
from .admin import my_admin_site
from . import views

urlpatterns = [
    # url(r'^time/', views.current_datetime),
    url(r'^$', views.index),
    url(r'^admin/', my_admin_site.urls),
    url(r'^employees/(?P<pk>[0-9]{6})/profile/$', views.my_profile, name='capstone'),
    url(r'^employees/profile/$', views.my_profile, name='capstone'),
    # url(r'^employees/(?P<year>[0-9]{4})/$', views.year_joined, name='capstone')
]
