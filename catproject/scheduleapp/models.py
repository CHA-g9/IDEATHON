from django.db import models
from django.db.models.fields import CharField, DateTimeField

# Create your models here.
class schedule(models.Model):
    event_name = models.CharField(max_length=50)
    event_date = models.DateTimeField()
    event_place = models.CharField(max_length=100)

    def __str__(self):
        return self.event_name