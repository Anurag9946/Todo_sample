from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    place = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

