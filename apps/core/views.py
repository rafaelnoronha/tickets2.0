import inspect

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets


class BaseModelViewSet(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None
    serializer_classes = None
    actions = None

    @action(
        methods=['patch'],
        detail=True,
        url_path='ativar-inativar',
        url_name='ativar-inativar',
        permission_classes=[action.get('ativar-inativar').get('permission_classes')]
    )
    def ativa_invativar(self, request, pk):
        model = self.get_object()
        action = self.actions.get(frame.f_code.co_name)
        frame = inspect.currentframe()

        serializer = action.get('serializer_class')(data=request.data)
        serializer.is_valid(raise_exception=True)

        model.ativo = serializer.data.get( 'ativo' )
        model.save()

        serializer = self.serializer_class(model)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if self.serializer_classes:
            return self.serializer_classes.get(self.action, self.serializer_class)
        
        return self.serializer_class
