# Similar objectives as "urls.py" to route the data to the consumers

from channels.auth import AuthMiddlewareStack   # hooking django auth system, forcing a user to log into the system prior to use the chat service
# AuthMiddlewareStack: but right now, we're going to utilize it to find out who the user is

from channels.routing import ProtocolTypeRouter, URLRouter

# from chatApp import routing
import chatApp.routing

# Instead of using "urlpatterns[]"; when WS request is being sent, route that using following; mapping of a protocolType
application = ProtocolTypeRouter({
    # wrap the URLs into the auth
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chatApp.routing.websocket_urlpatterns
        )
    ),
})