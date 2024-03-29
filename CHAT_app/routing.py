from django.urls import re_path
from CHAT_app import consumers
websocket_urlpatterns = [
    re_path(r'wss/socket-server/', consumers.ChatConsumer.as_asgi()),
    re_path(r'wss/(?P<room_name>[^/]+)/socket-server/', consumers.ChatConsumer.as_asgi()),
]

