from django.shortcuts import render

# Create your views here.
from .models import isplc , devices
from .serializers import isplcSerializer , devicesSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class devicesViewSet(viewsets.ModelViewSet):

    queryset = devices.objects.all()
    serializer_class = devicesSerializer
    permission_classes = (IsAuthenticated,)

class isplcViewSet(viewsets.ModelViewSet):
    #b = isplc.objects.get(id = 11)
    #b.delete()

    serializer_class = isplcSerializer
    lookup_field = 'userID'

    def perform_create(self, serializer):
        serializer.save(userID=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save(userID=self.request.user.id)

    queryset = isplc.objects.all()
    serializer_class = isplcSerializer
    permission_classes = (IsAuthenticated,)





