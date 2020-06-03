from django.db import models
from django.contrib.auth.models import User

class LineModel(models.Model):
    author = models.ForeignKey(
        User, db_column="user", on_delete=models.CASCADE)
    LineToken = models.CharField(max_length=9999)
     
class LineSettingsModel(models.Model):
    author = models.ForeignKey(
        User, db_column="user", on_delete=models.CASCADE)
    msg_Type = (
        (1,'Button'),
        (2,'Notify')
    )
    Contact_TYPES = (
        (1, 'Y'),
        (2, 'M')
    )
    msgType = models.PositiveSmallIntegerField(choices=msg_Type)
    msgContext = models.CharField(max_length=50)
    button1 = models.CharField(max_length=20, default="")
    button2 = models.CharField(max_length=20, default="")
    isPLC_ID = models.IntegerField()
    Contact_Type = models.PositiveSmallIntegerField(choices=Contact_TYPES)
    Contact_ID = models.PositiveIntegerField(default=0)
