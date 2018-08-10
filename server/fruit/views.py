from rest_framework import viewsets
from fruit.serializers import FruitSerializer
from fruit.models import Fruit


class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
