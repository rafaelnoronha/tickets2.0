from apps.core.serializers import BaseSerializer
from apps.core.filters import lookup_types_base

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


def action_ativar_inativar(viewClass):
    props_action = viewClass.action_ativar_inativar

    def decorator():
        class View(viewClass):
            @action(
                methods=['patch'],
                detail=True,
                url_path='ativar-inativar',
                url_name='ativar-inativar',
                permission_classes=[props_action.get('permission'),]
            )
            def ativar_inativar(self, request, pk):
                model = self.get_object()
                field = 'is_active' if hasattr(model, 'is_active') else 'ativo'

                serializer = props_action.get('serializer')(data=request.data)
                serializer.is_valid(raise_exception=True)

                setattr(model, field, serializer.data.get( field ))
                model.save()

                serializer = self.serializer_class(model)

                return Response(serializer.data, status=status.HTTP_200_OK)

        return View

    return decorator()

def fields_base_serializer(metaSerializerClass):
    def decorator():
        metaSerializerClass.Meta.fields += BaseSerializer.Meta.fields.copy()

        return metaSerializerClass

    return decorator()


def fields_base_filter_set(metaFilterSetClass):
    def decorator():
        metaFilterSetClass.Meta.fields.update(lookup_types_base)
        print(metaFilterSetClass.Meta.fields)

        return metaFilterSetClass

    return decorator()
