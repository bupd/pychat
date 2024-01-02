from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    name=models.CharField(max_length=20)
    slug=models.SlugField(max_length=10)

class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    message=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
