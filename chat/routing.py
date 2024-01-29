from django.urls import path, include
from .consumers import ChatConsumer

websocket_urlpattern = [
    path(
        "",
        ChatConsumer.as_asgi(),
    )
]
