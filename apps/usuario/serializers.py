from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import update_last_login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from user_agents import parse

from rest_framework import exceptions, serializers
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Usuario
from apps.auditoria.models import LogAutenticacao


class UsuarioSerializer(serializers.ModelSerializer):
    def validate_password(self, password):
        validate_password(password)

        return make_password(password)

    class Meta:
        model = Usuario
        fields = [
            'id',
            'username',
            'email',
            'is_active',
            'is_superuser',
            'authentication_failures',
            'last_login',
            'data_criacao',
            'hora_criacao',
            'data_alteracao',
            'hora_alteracao',
            'owner_id'
        ]
        read_only_fields = fields.copy()


class UsuarioListSerializer(UsuarioSerializer):
    class Meta(UsuarioSerializer.Meta):
        fields = [
            'id',
            'username',
            'email',
            'is_active',
            'is_superuser',
            'last_login',
            'owner_id'
        ]


class UsuarioPutPathSerializer(UsuarioSerializer):
    class Meta(UsuarioSerializer.Meta):
        read_only_fields = [field for field in UsuarioSerializer.Meta.read_only_fields if field not in ['email',]]


class UsuarioPostSerializer(UsuarioSerializer):
    class Meta(UsuarioSerializer.Meta):
        fields = UsuarioSerializer.Meta.fields.copy() + ['password',]
        read_only_fields = [field for field in UsuarioSerializer.Meta.read_only_fields if field not in [
            'username',
            'email',
            'password'
        ]]


class UsuarioTransformarAdminSerializer(UsuarioSerializer):
    class Meta(UsuarioSerializer.Meta):
        read_only_fields = read_only_fields = [field for field in UsuarioSerializer.Meta.read_only_fields if field not in ['is_superuser',]]
        extra_kwargs = {
            'is_superuser': {'allow_null': False, 'required': True}
        }


class UsuarioAtivarInativarSerializer(UsuarioSerializer):
    class Meta(UsuarioSerializer.Meta):
        read_only_fields = read_only_fields = [field for field in UsuarioSerializer.Meta.read_only_fields if field not in ['is_active',]]
        extra_kwargs = {
            'is_active': {'allow_null': False, 'required': True}
        }


class UsuarioRedefinirSenhaSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, required=True)
    password_confirmation = serializers.CharField(max_length=128, required=True)

    def validate_password(self, password):
        validate_password(password)

        return password

    def validate_password_confirmation(self, password_confirmation):
        validate_password(password_confirmation)

        return password_confirmation

    def validate(self, attrs):
        data = self.get_initial()

        if data.get('password') != data.get('password_confirmation'):
            raise serializers.ValidationError("O password e o password_confirmation devem ser iguais.")

        return attrs

    class Meta:
        fields = [
            'password',
            'password_confirmation'
        ]


class UsuarioAlterarSenhaSerializer(serializers.Serializer):
    current_password = serializers.CharField(max_length=128, required=True)
    new_password = serializers.CharField(max_length=128, required=True)
    new_password_confirmation = serializers.CharField(max_length=128, required=True)

    def validate_new_password(self, password):
        validate_password(password)

        return password

    def validate_new_password_confirmation(self, password_confirmation):
        validate_password(password_confirmation)

        return password_confirmation

    def validate(self, attrs):
        data = self.get_initial()

        if data.get('new_password') != data.get('new_password_confirmation'):
            raise serializers.ValidationError("O new_password e o new_password_confirmation devem ser iguais.")

        return attrs

    class Meta:
        fields = [
            'current_password',
            'new_password',
            'new_password_confirmation'
        ]


class ObterTokenSerializer(TokenObtainSerializer):
    def validate(self, attrs):
        user_model = get_user_model()
        max_num_fail_auth = user_model.MAX_NUM_FAIL_AUTH
        num_fail_auth_field = user_model.NUM_FAIL_AUTH_FIELD
        user_agent = parse(self.context.get('request').META.get('HTTP_USER_AGENT'))

        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            "password": attrs["password"],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        try:
            user = user_model.objects.get(username=attrs[self.username_field])

            if not self.user and user.is_active:
                user.__setattr__(num_fail_auth_field, user.__getattribute__(num_fail_auth_field) + 1)
                user.save()
                user.refresh_from_db()

                self.user = user if user.__getattribute__(num_fail_auth_field) >= max_num_fail_auth else None

        except Usuario.DoesNotExist:
            user = None

        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            if user:
                LogAutenticacao.objects.create(
                    lt_ip=self.context.get('request').META.get('REMOTE_ADDR'),
                    lt_user_agent=user_agent,
                    lt_usuario=user,
                    lt_autenticado='N',
                )

            if user and not user.is_active:
                raise exceptions.AuthenticationFailed(
                    'Nenhuma conta ativa encontrada com as credenciais fornecidas',
                    "usuario_inativo",
                )
            elif self.user and self.user.__getattribute__(num_fail_auth_field) >= max_num_fail_auth:
                raise exceptions.AuthenticationFailed(
                    'Usuário bloqueado, máximo de tentativas falhas de login atingido',
                    "usuario_bloqueado",
                )
            else:
                raise exceptions.AuthenticationFailed(
                    self.error_messages["no_active_account"],
                    "no_active_account",
                )
        else:
            LogAutenticacao.objects.create(
                lt_ip=self.context.get('request').META.get('REMOTE_ADDR'),
                lt_user_agent=user_agent,
                lt_usuario=user,
                lt_autenticado='S',
            )

            if user and user.__getattribute__(num_fail_auth_field) != 0:
                user.__setattr__(num_fail_auth_field, 0)
                user.save()


        return {}


class ObterParTokensSerializer(ObterTokenSerializer):
    @classmethod
    def get_token(cls, user):
        token = RefreshToken.for_user(user)
        # token['teste'] = 123

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class AtualizacaoTokenSerializer(TokenRefreshSerializer):
    refresh = serializers.CharField()
    access = serializers.ReadOnlyField()

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])

        data = {'access': str(refresh.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()

            data['refresh'] = str(refresh)

        return data
