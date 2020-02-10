from django.db import models

# Create your models here.

class isplc(models.Model):
    userID = models.IntegerField(default=0)
    Xcontact = models.TextField()
    Ycontact = models.TextField()
    Mcontact = models.TextField()
    Dcontact = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "isplcs"