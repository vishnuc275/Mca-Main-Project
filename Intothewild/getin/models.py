from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Userreg(models.Model):
    Role = models.CharField(max_length=100, blank=True, null=True)
    Exp = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    housename = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "userreg"



class Fb(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    currentdate = models.DateField(default=timezone.now)
    feedback = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = "fb"


class Images(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    amount = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='gallery/%y%m%d', blank=True, null=True)
    class Meta:
        db_table = "image"

class Staffreg(models.Model):
    license = models.ImageField(upload_to='license/%y%m%d', blank=True, null=True)
    Role = models.CharField(max_length=100, blank=True, null=True, default='staff')
    Exp = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(max_length=100, blank=True, null=True)
    housename = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True, default='pending')

    class Meta:
        db_table = "staffreg"

class Login(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True)
    password1 = models.CharField(max_length=100, blank=True, null=True)
    Role = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)



    class Meta:
        db_table = "login"
