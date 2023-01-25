from rest_framework.routers import SimpleRouter

from .views import UsuarioViewSet, GrupoPermissoesUsuarioViewSet, PermissaoUsuarioViewSet


usuario_router = SimpleRouter()
usuario_router.register('', UsuarioViewSet)

router_grupo_permissoes_usuario = SimpleRouter()
router_grupo_permissoes_usuario.register('', GrupoPermissoesUsuarioViewSet)

router_permissao_usuario = SimpleRouter()
router_permissao_usuario.register('', PermissaoUsuarioViewSet)
