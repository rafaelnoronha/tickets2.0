from rest_framework.routers import SimpleRouter

from .views import EmpresaViewSet


empresa_router = SimpleRouter()
empresa_router.register('', EmpresaViewSet)
