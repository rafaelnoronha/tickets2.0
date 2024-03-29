from rest_framework.permissions import BasePermission


class EmpresaAtivarInativarPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perms(['empresa.ativar_inativar',]):
            return True

        return False
