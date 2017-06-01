# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    addr = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    skills = models.CharField(max_length=500)
    interests = models.CharField(max_length=500)
