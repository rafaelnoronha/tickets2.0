from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    max_limit = 100
