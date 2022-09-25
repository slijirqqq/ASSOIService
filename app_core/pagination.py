from rest_framework.pagination import PageNumberPagination as OriginalPageNumberPagination


class PageNumberPagination(OriginalPageNumberPagination):
    page_size = 50
    max_page_size = 100
