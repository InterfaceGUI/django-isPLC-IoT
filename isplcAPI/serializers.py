from rest_framework import serializers
from .models import isplc,devices
from rest_framework.authtoken.models import Token
from dashboard.models import control
from app.models import LineModel,LineSettingsModel

class isplcSerializer(serializers.ModelSerializer):

    class Meta:
        model = isplc
        # fields = '__all__'
        fields = ('id', 'userID','isPLC_ID','Xcontact', 'Ycontact', 'Mcontact', 'Dcontact','last_modify_date', 'created')

class devicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = devices
        # fields = '__all__'
        fields = ('id', 'author','device_name', 'displc_count', 'device_IP', 'last_modify_date')

class TokenAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ("__all__")

class ControlContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = control
        fields = ("__all__")


class LineTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineModel
        fields = ("LineToken",)

class LineSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineSettingsModel
        fields = ("msgType","msgContext","button1","button2","isPLC_ID","Contact_Type","Contact_ID",)
