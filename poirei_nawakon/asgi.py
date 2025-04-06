
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poirei_nawakon.settings')

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    'http': django_asgi_app,
    
    # WebSocket handler - can be configured later if needed
    # 'websocket': AuthMiddlewareStack(
    #     URLRouter(
    #         # Add websocket routing here if needed
    #     )
    # ),
})