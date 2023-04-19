from rest_framework import mixins, viewsets


class GenresCategoriesMixin(
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    pass
