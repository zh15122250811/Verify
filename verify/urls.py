from django.conf.urls import url, include
from django.contrib import admin

from verify import views

urlpatterns = [
    url(r'^get_verify/', views.get_verify, name="get_verify"),
    url(r'^verify/', views.get_verify, name="verify"),

    url(r'^logUser/', views.logUser, name="logUser"),
    url(r'^dologin/', views.dologin, name="dologin"),
]
