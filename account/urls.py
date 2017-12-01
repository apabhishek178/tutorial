from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login, logout
urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'account/Login.html'}),
    url(r'^logout/$', logout, {'template_name': 'account/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
]