from django.db import models
import os
import datetime

# Create your models here.

def get_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename) 

class Courses(models.Model):
    CourseName = models.CharField(max_length=20)
    Duration = models.CharField(max_length=20)

    def __str__(self):
        return self.CourseName

class Applicant(models.Model):
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    genderOptions = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    Gender = models.CharField(
        max_length=2,
        choices = genderOptions,
        default = 'M'
    )
    Address = models.CharField(max_length=20)
    Email = models.EmailField(max_length=25)
    Contact = models.CharField(max_length=15)
    School = models.CharField(max_length=20)
    Section = models.CharField(max_length=20)
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.Fname

class Contact(models.Model):
    Email = models.EmailField(max_length=25)
    Phone = models.CharField(max_length=15)
    Message = models.CharField(max_length=500)

    def __str__(self):
        return self.Email

class TrainningProgram(models.Model):
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=200)
    Picture = models.ImageField(upload_to=get_path, null=True, blank=True)

    def __str__(self):
        return self.Title

class GirlsInCode(models.Model):
    Names = models.CharField(max_length=25)
    Description = models.CharField(max_length=200)
    Picture = models.ImageField(upload_to=get_path, null=True, blank=True)

    def __str__(self):
        return self.Names

class JuniorProgrammer(models.Model):
    Names = models.CharField(max_length=25)
    Description = models.CharField(max_length=200)
    Picture = models.ImageField(upload_to=get_path, null=True, blank=True)

    def __str__(self):
        return self.Names

class ItService(models.Model):
    Title = models.CharField(max_length=25)
    IconService = models.ImageField(upload_to=get_path, null=True, blank=True)
    Content = models.CharField(max_length=200)

    def __str__(self):
        return self.Title

class Project(models.Model):
    Title = models.CharField(max_length=30)
    Description = models.CharField(max_length=200)
    Picture = models.ImageField(upload_to=get_path, blank=True, null=True)

    def __str__(self):
        return self.Title

