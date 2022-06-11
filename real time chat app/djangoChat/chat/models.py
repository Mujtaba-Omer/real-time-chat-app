from django.db import models
from datetime import datetime

class Room(models.Model):
    room_name = models.CharField(max_length=100)


class Massage(models.Model):
    context = models.CharField(max_length=10000)
    room = models.CharField(max_length=500)
    user = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now, blank=True)
