from django.db import models
from django.utils import timezone

class Seller(models.Model):

    name = models.CharField(max_length=100)
    cnic = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=32)

    confirm_password = models.CharField(max_length=32)
    address = models.CharField(max_length=100)
    experience = models.TextField()
    min_charges = models.IntegerField()
    max_charges = models.IntegerField()
   # profile_pic = models.ImageField()
    other_detail = models.TextField()

    def __str__(self):
        return self.name

