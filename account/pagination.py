from rest_framework import pagination

class BasePagination(pagination.PageNumberPagination):
    page_size = 30