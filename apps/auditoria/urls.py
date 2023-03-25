from rest_framework.routers import SimpleRouter

from .views import LogAutenticacaoViewSet


log_authenticacao_router = SimpleRouter()
log_authenticacao_router.register('', LogAutenticacaoViewSet)
