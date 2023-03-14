from rest_framework.permissions import BasePermission


class UsuarioAtivarInativarPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perms(['usuario.ativar_inativar',]):
            return True

        return False


class TransformaAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perms(['usuario.transformar_admin',]):
            return True

        return False


class TransformaGerentePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perms(['usuario.transformar_gerente',]):
            return True

        return False


class DesbloquearPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perms(['usuario.desbloquear',]):
            return True

        return False
    

class ClassificacaoUsuarioAtivarInativarPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perms(['usuario.ativar_inativar',]):
            return True

        return False
    

class UsuarioEmpresaAtivarInativarPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perms(['usuario.ativar_inativar',]):
            return True

        return False
