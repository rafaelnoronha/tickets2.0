from rest_framework.routers import SimpleRouter

from .views import (
    UsuarioViewSet, GrupoPermissoesUsuarioViewSet, PermissaoUsuarioViewSet,
    ClassificacaoUsuarioViewSet, UsuarioEmpresaViewSet
)


usuario_router = SimpleRouter()
usuario_router.register('', UsuarioViewSet)

router_grupo_permissoes_usuario = SimpleRouter()
router_grupo_permissoes_usuario.register('', GrupoPermissoesUsuarioViewSet)

router_permissao_usuario = SimpleRouter()
router_permissao_usuario.register('', PermissaoUsuarioViewSet)

classificacao_usuario_router = SimpleRouter()
classificacao_usuario_router.register('', ClassificacaoUsuarioViewSet)

usuario_empresa_router = SimpleRouter()
usuario_empresa_router.register('', UsuarioEmpresaViewSet)
