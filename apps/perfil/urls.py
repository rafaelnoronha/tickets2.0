from rest_framework.routers import SimpleRouter

from .views import PerfilUsuarioViewSet


perfil_usuario_router = SimpleRouter()
perfil_usuario_router.register('', PerfilUsuarioViewSet)
