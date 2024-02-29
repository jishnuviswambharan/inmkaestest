from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=250)
    priority=models.IntegerField()
    desc=models.CharField(max_length=300)
    date=models.DateField()

    def __str__(self):
        return self.name