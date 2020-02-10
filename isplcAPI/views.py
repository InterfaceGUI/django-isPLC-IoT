from django.shortcuts import render

# Create your views here.
from .models import isplc
from .serializers import isplcSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class isplcViewSet(viewsets.ModelViewSet):
    queryset = isplc.objects.all()
    serializer_class = isplcSerializer
    permission_classes = (IsAuthenticated,)