from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Problem(models.Model):
    q_id = models.IntegerField(primary_key = True)
    topic = models.CharField(max_length=30)
    q_name = models.CharField(max_length=30)
    link = models.URLField(max_length=200)

class Sources(models.Model):
    id = models.IntegerField(primary_key = True)
    topic = models.CharField(max_length=30)
    link = models.URLField(max_length=200)

