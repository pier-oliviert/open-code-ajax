from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from todos.models import Todo

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', "todos.views.list"),
    (r'^todo/(?P<pk>\d+)/done$', "todos.views.done")
)