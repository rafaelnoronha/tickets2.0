from rest_framework.permissions import BasePermission


class PoliticaPrivacidadeAtivarInativarPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perms(['lgpd.ativar_inativar',]):
            return True

        return False