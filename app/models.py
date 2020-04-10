from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user   = models.ForeignKey(
        User, db_column="user", on_delete=models.CASCADE)
    avatar = models.ImageField()