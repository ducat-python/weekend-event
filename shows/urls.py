from django.conf.urls import url, include

from .views import show_list

urlpatterns = [

    url(r'^list/', show_list, name='list'),
]
