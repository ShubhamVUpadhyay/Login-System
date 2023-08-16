from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Userinfo(models.Model):
    user=models.OneToOneField(User,on_delete=callable)
