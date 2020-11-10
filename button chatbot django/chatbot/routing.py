from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter

from .consumers import ChatConsumer

application = ProtocolTypeRouter({
	'websocket': URLRouter([
		url("",ChatConsumer.as_asgi() )
		]
		)
	})