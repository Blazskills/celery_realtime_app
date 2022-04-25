from django.urls import path
from .consumers import JokersConsumer

ws_urlpatterns = [
    path('ws/jokes/', JokersConsumer.as_asgi()),
]