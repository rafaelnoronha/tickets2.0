from rest_framework.routers import SimpleRouter

from .views import UsuarioViewSet


usuario_router = SimpleRouter()
usuario_router.register(r'', UsuarioViewSet)
