from django.urls import path
from django.conf.urls import include, url
from myapp.views import hello

urlpatterns = [
    url(r'^hello/$', hello, name = 'hello'),
]