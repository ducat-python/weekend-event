from django.conf.urls import url, include

from .views import show_list, show_create

urlpatterns = [

    url(r'^list/', show_list, name='list'),
    url(r'^create/', show_create, name='create'),
]
