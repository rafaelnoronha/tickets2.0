from django.contrib.auth.password_validation import MinimumLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _, ngettext



class MinimumLengthValidatorCustom(MinimumLengthValidator):
    """
    Validate whether the password is of a minimum length.
    """
    def __init__(self):
        super().__init__(6)


class ComprimentoMaximoValidator:
    """
    Valida se a senha tem o comprimento máximo.
    """
    def __init__(self, comprimento_maximo=32):
        self.comprimento_maximo = comprimento_maximo

    def validate(self, password, user=None):
        if len(password) > self.comprimento_maximo:
            raise ValidationError(
                f"Esta senha é muito longa. Deve conter no máximo {self.comprimento_maximo} caracteres.",
                code='senha_muito_longa',
                params={'comprimento_maximo': self.comprimento_maximo},
            )

    def get_help_text(self):
        return f"Sua senha deve conter no máximo {self.comprimento_maximo} caracteres"
