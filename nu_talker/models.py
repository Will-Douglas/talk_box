from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey
# Create your models here.

class NuTalker(AbstractUser):
    name = models.CharField(max_length=150)
    age = models.IntegerField(null=True)
    hometown = models.CharField(max_length=150)
    connection = models.ManyToManyField("self", symmetrical=False)