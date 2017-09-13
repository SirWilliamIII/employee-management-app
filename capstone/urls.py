from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^employees/profile/list/$', views.ProfileListView.as_view(), name='profile_list'),
    url(r'^employees/(?P<pk>[0-9]+)/profile/$', views.ProfileDetailView.as_view(), name='profile_detail'),
    url(r'^employees/profile/create/$', views.ProfileCreateView.as_view(), name='profile_create'),
    url(r'^employees/(?P<pk>[0-9]+)/profile/$', views.ProfileUpdateView.as_view(), name='my_profile_update'),
    url(r'^employees/(?P<pk>[0-9]+)/profile/$', views.ProfileDeleteView.as_view(), name='my_profile_delete'),
]
