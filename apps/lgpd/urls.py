from rest_framework.routers import SimpleRouter

from .views import PoliticaPrivacidadeViewSet, ConsentimentoPoliticaPrivacidadeViewSet


politica_privacidade_router = SimpleRouter()
politica_privacidade_router.register('', PoliticaPrivacidadeViewSet)

consentimento_politica_privacidade_router = SimpleRouter()
consentimento_politica_privacidade_router.register('', ConsentimentoPoliticaPrivacidadeViewSet)
