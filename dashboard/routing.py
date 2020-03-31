from django.urls import path
from dashboard.consumer import LiveConsumer

websocket_urlpatterns = [
    path('ws/Client/<str:name>/<str:ID>', LiveConsumer),
]