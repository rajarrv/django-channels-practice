from django.urls import re_path
from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    url(r'species/$', consumers.ChatConsumer.as_asgi()),
]