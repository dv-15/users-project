from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll_number = models.IntegerField(default=None)
    date_of_birth = models.DateField(default=None)
    email = models.CharField(max_length=20)
    phone_number = models.IntegerField(default=None)
    address = models.CharField(max_length=30)

    class Meta:
        db_table = "students"