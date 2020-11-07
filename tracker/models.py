from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

class classroom(models.Model):
    class_code = models.CharField(max_length=30)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    proxies_marked = models.IntegerField(default=0)
    def __str__(self):
        return "%s" % (self.class_code)

class lecture_copy(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture_name = models.CharField(max_length=100, default="None")
    lecture_count = models.IntegerField(default=0)
    tot_lecture_count = models.IntegerField(default=0)

    def __str__(self):
        return "%s" %   (self.student) + " lecture--> "  + (self.lecture_name)

class sdata(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    slot1 = models.IntegerField(default=0)
    slot2 = models.IntegerField(default=0)
    slot3 = models.IntegerField(default=0)
    slat = models.FloatField(default=0.0)
    slong = models.FloatField(default=0.0)

class Lecture(models.Model):

    monday_slot1_name = models.CharField(max_length=100, default="None")
    monday_slot1_latitude = models.FloatField(default=0.0)
    monday_slot1_longitude = models.FloatField(default=0.0)
    monday_slot2_name = models.CharField(max_length=100, default="None")
    monday_slot2_latitude = models.FloatField(default=0.0)
    monday_slot2_longitude = models.FloatField(default=0.0)
    monday_slot3_name = models.CharField(max_length=100, default="None")
    monday_slot3_latitude = models.FloatField(default=0.0)
    monday_slot3_longitude = models.FloatField(default=0.0)

    tuesday_slot1_name = models.CharField(max_length=100, default="None")
    tuesday_slot1_latitude = models.FloatField(default=0.0)
    tuesday_slot1_longitude = models.FloatField(default=0.0)
    tuesday_slot2_name = models.CharField(max_length=100, default="None")
    tuesday_slot2_latitude = models.FloatField(default=0.0)
    tuesday_slot2_longitude = models.FloatField(default=0.0)
    tuesday_slot3_name = models.CharField(max_length=100, default="None")
    tuesday_slot3_latitude = models.FloatField(default=0.0)
    tuesday_slot3_longitude = models.FloatField(default=0.0)

    wednesday_slot1_name = models.CharField(max_length=100, default="None")
    wednesday_slot1_latitude = models.FloatField(default=0.0)
    wednesday_slot1_longitude = models.FloatField(default=0.0)
    wednesday_slot2_name = models.CharField(max_length=100, default="None")
    wednesday_slot2_latitude = models.FloatField(default=0.0)
    wednesday_slot2_longitude = models.FloatField(default=0.0)
    wednesday_slot3_name = models.CharField(max_length=100, default="None")
    wednesday_slot3_latitude = models.FloatField(default=0.0)
    wednesday_slot3_longitude = models.FloatField(default=0.0)

    thrusday_slot1_name = models.CharField(max_length=100, default="None")
    thrusday_slot1_latitude = models.FloatField(default=0.0)
    thrusday_slot1_longitude = models.FloatField(default=0.0)
    thrusday_slot2_name = models.CharField(max_length=100, default="None")
    thrusday_slot2_latitude = models.FloatField(default=0.0)
    thrusday_slot2_longitude = models.FloatField(default=0.0)
    thrusday_slot3_name = models.CharField(max_length=100, default="None")
    thrusday_slot3_latitude = models.FloatField(default=0.0)
    thrusday_slot3_longitude = models.FloatField(default=0.0)

    friday_slot1_name = models.CharField(max_length=100, default="None")
    friday_slot1_latitude = models.FloatField(default=0.0)
    friday_slot1_longitude = models.FloatField(default=0.0)
    friday_slot2_name = models.CharField(max_length=100, default="None")
    friday_slot2_latitude = models.FloatField(default=0.0)
    friday_slot2_longitude = models.FloatField(default=0.0)
    friday_slot3_name = models.CharField(max_length=100, default="None")
    friday_slot3_latitude = models.FloatField(default=0.0)
    friday_slot3_longitude = models.FloatField(default=0.0)

    student = models.ForeignKey(User, on_delete=models.CASCADE) #1 to many

    def __str__(self):
         return "%s" % (self.student) + "--> timetable"
