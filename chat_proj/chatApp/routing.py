from django.urls import re_path   # relative path
from . import consumers

# "websocket_urlpatterns[]" will be route to consumers
websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer),   # similar to "chat_room" in the "urls.py" of this file
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatRoomConsumer.as_asgi()),   # similar to "chat_room" in the "urls.py" of this file
]