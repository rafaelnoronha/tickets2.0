from rest_framework import viewsets


class BaseModelViewSet(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None
    serializer_classes = None

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
