from django.db import models

# Create your models here.

class isplc(models.Model):

    userID = models.IntegerField(default=0)
    isPLC_ID = models.IntegerField(default=0)
    Xcontact = models.CharField(max_length=6)
    Ycontact = models.CharField(max_length=6)
    Mcontact = models.CharField(max_length=50)
    Dcontact = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
#FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF,FFF
    class Meta:
        db_table = "isplcs"

