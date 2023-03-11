from rest_framework.routers import SimpleRouter

from .views import ParametroViewSet


parametro_router = SimpleRouter()
parametro_router.register('', ParametroViewSet)
