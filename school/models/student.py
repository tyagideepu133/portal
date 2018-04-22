from django.db import models
from .auth import CustomUser
from .school import SchoolModel
from django.utils import timezone
import os, time, uuid
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

def upload_location_student(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s/%s/%s/%s.%s" %("images", "school", instance.school, "students", instance.id, extension)

def upload_location_enquiry(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s/%s/%s/%s.%s" %("images", "school",instance.school, "enquiry", instance.id, extension)
    
def upload_location_registration(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s/%s/%s/%s.%s" %("images", "school",instance.school, "registration", instance.id, extension)

#completed
# Admin
# teacher(self) student(get)
class StudentModel(models.Model):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )

    id = models.BigIntegerField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=False)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    father_name = models.CharField(max_length=100, null=False)
    mother_name = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to=upload_location_student)
    date_of_birth = models.DateField(null=False)
    blood_group = models.CharField(max_length=10, null=True)
    birth_place = models.CharField(max_length=30, null=True, blank=True)
    nationality = models.CharField(max_length=30, null=True)
    mother_tongue = models.CharField(max_length=30, null=True)
    category = models.CharField(max_length=30, null=True)
    religion = models.CharField(max_length=30, null=True)
    caste = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    pin = models.BigIntegerField(null=True)
    aadhar_number = models.IntegerField(null=True)
    phone_no = models.BigIntegerField(null=False)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=False)
    father_phone_no = models.BigIntegerField(null=True)
    mother_phone_no = models.BigIntegerField(null=True)
    father_aadhar = models.BigIntegerField(null=True)
    mother_aadhar = models.BigIntegerField(null=True)
    perm_address = models.CharField(max_length=500, null=False) 
    temp_address = models.CharField(max_length=500, null=True)
    father_profession = models.CharField(max_length=50, null=False)
    mother_profession = models.CharField(max_length=50, null=False)
    father_office_address = models.CharField(max_length=500, null=True)
    mother_office_address = models.CharField(max_length=500, null=True)
    pervious_school_name = models.CharField(max_length=200, null=True)
    pervious_school_address = models.CharField(max_length=500, null=True)
    pervious_qualification = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.first_name) + " " +str(self.last_name)

# Admin
class EnquiryModel(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )

    first_name = models.CharField(max_length=50, null=False)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100, null=False)
    mother_name = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to=upload_location_enquiry)
    date_of_birth = models.DateField(null=False)
    aadhar_number = models.IntegerField(null=True)
    phone_no = models.BigIntegerField(null=False)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=False)
    current_address = models.CharField(max_length=500, null=True)
    current_qualification = models.CharField(max_length=50, null=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.first_name) + " " +str(self.last_name)

# Admin
class RegistrationModel(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )

    def path_and_rename(self, instance, filename):
        upload_to = 'photos/registration'
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)
    
    first_name = models.CharField(max_length=50, null=False)
    middle_name = models.CharField(max_length=30, null=True)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=30, null=True)
    father_name = models.CharField(max_length=100, null=False)
    mother_name = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to=upload_location_registration)
    date_of_birth = models.DateField(null=False)
    aadhar_number = models.IntegerField(null=True)
    phone_no = models.BigIntegerField(null=False)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=False)
    current_address = models.CharField(max_length=500, null=True)
    current_qualification = models.CharField(max_length=50, null=True)
    date = models.DateField(default=timezone.now)
    registration_fee = models.IntegerField(null=True)
    apply_for = models.CharField(max_length=100, null=False)
    is_shortlisted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.first_name) + " " +str(self.last_name)