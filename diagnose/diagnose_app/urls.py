from django.conf.urls.defaults import *
from diagnose_app import views
urlpatterns = patterns('',
    (r'^$', views.index, name='index'),
)
