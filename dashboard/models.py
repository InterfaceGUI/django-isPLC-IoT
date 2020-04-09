from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class control(models.Model):
    #author = models.ForeignKey(User, db_column="user", on_delete=models.CASCADE)
    uid = models.IntegerField()
    Control_TYPES = (
        (1, 'Button'),
        (2, 'Toggle Switches'),
        (3, 'Gauge(Not done yet.)'),
        (4, 'Green Lamp'),
        (5, 'Yellow Lamp'),
        (6, 'Red Lamp'),
        (7, 'Numerical'),
    )
    Contact_TYPES = (
        (1, 'X'),
        (2, 'Y'),
        (3, 'M'),
        (4, 'D'),
    )
    index = models.IntegerField(default=0)
    control_type = models.PositiveSmallIntegerField(choices=Control_TYPES)
    Name = models.CharField(max_length=40)
    Text = models.CharField(max_length=40, default="")
    isPLC_ID = models.IntegerField()
    Contact_Type = models.PositiveSmallIntegerField(choices=Contact_TYPES)
    Contact_ID = models.IntegerField()


