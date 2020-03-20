from django.urls import path

from . import views
from mysite.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('', views.hello, name='home'),
]