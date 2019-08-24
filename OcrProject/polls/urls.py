from django.conf.urls import url

from . import views

urlpatterns = [
    'OcrProject.polls.views',
    url(r'^list/$', 'list', name='list'),
]
