from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=23)
    email = models.CharField(max_length=50 ,unique=True)
    password = models.CharField(max_length=35 ,null=True)

    def __str__(self):
        return self.name


