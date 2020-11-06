from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

class classroom(models.Model):
    class_code = models.CharField(max_length=30)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.class_code)
