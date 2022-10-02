from django.db import models

# Create your models here.

class Personal(models.Model):
    name = models.CharField(max_length=100,verbose_name="Name")
    age = models.IntegerField(verbose_name="Age")
    gender = models.CharField(max_length=100,verbose_name="Gender")

    def __str__(self):
        return self.name
