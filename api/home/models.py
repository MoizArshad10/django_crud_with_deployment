from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=12)
    lastname = models.CharField(max_length=12)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.firstname