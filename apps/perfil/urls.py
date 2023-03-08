from rest_framework.routers import SimpleRouter

from .views import PerfilUsuarioViewSet, PerfilUsuarioEmpresaViewSet, ClassificacaoPerfilViewSet


perfil_usuario_router = SimpleRouter()
perfil_usuario_router.register('', PerfilUsuarioViewSet)

perfil_usuario_empresa_router = SimpleRouter()
perfil_usuario_empresa_router.register('', PerfilUsuarioEmpresaViewSet)

classificacao_usuario_router = SimpleRouter()
classificacao_usuario_router.register('', ClassificacaoPerfilViewSet)
