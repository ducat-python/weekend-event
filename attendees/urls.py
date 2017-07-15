from django.conf.urls import url

from .views import register_attendee

urlpatterns = [

    url(r'^register/', register_attendee, name='register'),
]
