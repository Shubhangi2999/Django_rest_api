from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/partners/$', views.partners_list),
    url(r'^api/partners/details/$', views.partners_detail),
]