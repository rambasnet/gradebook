from django.db import models

# Create your models here.
class Grade(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    test1 = models.FloatField(default=0)
    test2 = models.FloatField(default=0)
    test3 = models.FloatField(default=0)

