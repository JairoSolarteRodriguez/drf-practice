# from rest_framework.views import APIView, Response
from rest_framework import viewsets

from ingredients import serializer, models

class IngredientsViewSet(viewsets.ModelViewSet):
    """ creata a ingredient """
    serializer_class = serializer.IngredientSerializer
    queryset = models.Ingredient.objects.all()