from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^client/(\d{2}\-\d{3}\-\d{3}\-\d{2})$', views.client, name='client'),
]