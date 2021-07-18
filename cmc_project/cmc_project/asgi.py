"""
ASGI config for cmc_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# from coins.routing import ws_urlpatterns
from django.urls import path

from .consumers import CoinsConsumer

ws_urlpatterns = [
    path('ws/coins/', CoinsConsumer.as_asgi())
]

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cmc_project.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})

