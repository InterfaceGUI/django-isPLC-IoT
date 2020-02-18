from rest_framework import serializers
from .models import isplc


class isplcSerializer(serializers.ModelSerializer):

    class Meta:
        model = isplc
        # fields = '__all__'
        fields = ('id', 'userID','isPLC_ID','Xcontact', 'Ycontact', 'Mcontact', 'Dcontact','last_modify_date', 'created')