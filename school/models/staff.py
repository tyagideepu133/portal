from django.db import models
from django.utils import timezone
from django.conf import settings
from .school import SchoolModel
from .auth import CustomUser


# Admin
class StaffModel(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=30, null=True)
    father_name = models.CharField(max_length=100, null=False)
    mother_name = models.CharField(max_length=100, null=False)
    date_of_birth = models.DateField(null=False)
    sex = models.CharField(max_length=20, choices=GENDER_CHOICES, null=False)
    phone_no_1 = models.BigIntegerField(null=False)
    phone_no_2 = models.BigIntegerField(null=False)
    perm_address = models.CharField(max_length=500, null=False) 
    temp_address = models.CharField(max_length=500, null=False)
    date_of_hiring = models.DateField(null=False)
    higest_education = models.CharField(null=False, max_length=20)
    email = models.EmailField(null=False)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)