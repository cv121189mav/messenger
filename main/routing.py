# chat/routing.py
from django.urls import path

from . import consumers

urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer),
]
