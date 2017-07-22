from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Show(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

