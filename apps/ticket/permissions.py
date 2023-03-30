from rest_framework.permissions import BasePermission


class AgrupamentoAtivarInativarPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perms(['ticket.ativar_inativar',]):
            return True

        return False
