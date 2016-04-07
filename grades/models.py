from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    test1 = models.FloatField(default=0)
    test2 = models.FloatField(default=0)
    test3 = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name
