from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_page),
    url(r'^action_register$', views.action_register),
    url(r'^action_login$', views.action_login),
    url(r'^success$', views.success_page),
]