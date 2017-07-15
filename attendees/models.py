from django.db import models

from shows.models import Show


# Create your models here.

class Attendee(models.Model):
    show = models.ForeignKey(Show)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
