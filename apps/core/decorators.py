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