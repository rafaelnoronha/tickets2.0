from rest_framework import viewsets, mixins


class EssentialModelViewSet(viewsets.GenericViewSet):
    queryset = None
    serializer_class = None
    serializer_classes = None
    action_ativar_inativar = {
        'permission': None,
        'serializer': None
    }

    def get_serializer_class(self):
        if self.serializer_classes:
            return self.serializer_classes.get(self.action, self.serializer_class)
        
        return self.serializer_class


class BaseModelViewSet(
        mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
        mixins.UpdateModelMixin, mixins.DestroyModelMixin, EssentialModelViewSet
    ):
    pass
