from django.conf.urls import url
from qa.views import question
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<num>\d+)/$', question),
]
