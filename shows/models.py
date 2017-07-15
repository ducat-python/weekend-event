from django.db import models

# Create your models here.

class Show(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

