"""tickets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView

from apps.usuario.views import ObterParTokensView
from apps.usuario.urls import usuario_router

api_v1 = 'api/v1'

urlpatterns = [
    path(f"{api_v1}/token/", ObterParTokensView.as_view(), name='token_obtain_pair'),
    path(f"{api_v1}/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path(f"{api_v1}/usuario/", include(usuario_router.urls)),
]
