from rest_framework.permissions import BasePermission


class PerfilUsuarioAtivarInativarPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perms(['perfil.ativar_inativar',]):
            return True

        return False