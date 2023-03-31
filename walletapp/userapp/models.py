from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Extends the User model from django.contrib.auth.models

class User(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"[{self.id}] {self.first_name} {self.middle_name} {self.last_name}"
