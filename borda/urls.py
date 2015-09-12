from borda import views

from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^thread(?P<thread_id>[0-9]+)/$', views.thread, name='thread'),
]
