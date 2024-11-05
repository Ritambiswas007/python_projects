from django.db import models

# Create your models here.
class Student(models.Model):
    # AutoField is default for primary key, so no need to explicitly define it
    name = models.CharField(max_length=255)  # max_length is required for CharField
    age = models.IntegerField(default=18)  # Use IntegerField instead of integer()
    email = models.EmailField()

    def __str__(self):
        return self.name  # Optional: for easy representation in Django Admin

class Product(models.Model):
    # AutoField is default for primary key
    name = models.CharField(max_length=100)  # max_length is required for CharField
    price = models.IntegerField()  # Use IntegerField instead of integer()

    def __str__(self):
        return self.name  # Optional: for easy representation in Django Admin
