# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    fisrt_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    user_id=models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50)
    state=models.CharField(max_length=100)
    Country=models.CharField(max_length=100)

    def __str__(self):
        return self.fisrt_name+' '+self.last_name



