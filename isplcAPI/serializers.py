from rest_framework import serializers
from .models import isplc,devices


class isplcSerializer(serializers.ModelSerializer):

    class Meta:
        model = isplc
        # fields = '__all__'
        fields = ('id', 'userID','isPLC_ID','Xcontact', 'Ycontact', 'Mcontact', 'Dcontact','last_modify_date', 'created')

class devicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = devices
        # fields = '__all__'
        fields = ('id', 'author','device_name','device_ID', 'displc_count', 'device_IP', 'last_modify_date')