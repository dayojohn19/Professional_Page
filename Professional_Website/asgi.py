# isort: skip_file
"""
ASGI config for Professional_Website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
# import CHAT_app.routing 
import CHAT_app.routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Professional_Website.settings')
import django
django.setup()
from channels.auth import AuthMiddlewareStack
# application = get_asgi_application()
application = ProtocolTypeRouter({
    # 'http':get_asgi_application(),
    'https':get_asgi_application(),

     'websocket':AuthMiddlewareStack(
         URLRouter(
            #  CHAT_app.routing.websocket_urlpatterns
             CHAT_app.routing.websocket_urlpatterns
         )
     ),
})

