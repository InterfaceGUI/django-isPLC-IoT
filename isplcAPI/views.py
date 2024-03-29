from django.shortcuts import render

# Create your views here.
from .models import isplc , devices
from .serializers import isplcSerializer , devicesSerializer , TokenAuthorSerializer , ControlContextSerializer ,LineTokenSerializer,LineSettingSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from dashboard.models import control
from app.models import LineModel,LineSettingsModel
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


class TokenAuthorView(viewsets.ReadOnlyModelViewSet):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = TokenAuthorSerializer
    #queryset = Token.objects.all()
    #def dispatch(self, *args, **kwargs):
    #   
    #   queryset = Token.objects.get(user=self.request.user.id)
    #   
    #   response = super(TokenAuthorView, self).dispatch(*args, **kwargs)
    #
    #        return response

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Token.objects.all()
        queryset = queryset.filter(user=self.request.user.id)
        return queryset

class ControlContextView(viewsets.ReadOnlyModelViewSet):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = ControlContextSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = control.objects.all()
        queryset = queryset.filter(uid=self.request.user.id)
        
        

        return queryset

class lineTokenView(viewsets.ReadOnlyModelViewSet):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = LineTokenSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = LineModel.objects.all()
        queryset = queryset.filter(author=self.request.user)
    
        return queryset

class lineSettingView(viewsets.ReadOnlyModelViewSet):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = LineSettingSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """

        queryset = LineSettingsModel.objects.filter(author=self.request.user)
    
        return queryset
