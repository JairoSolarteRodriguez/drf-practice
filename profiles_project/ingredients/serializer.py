from rest_framework import serializers

from ingredients import models

class IngredientSerializer(serializers.ModelSerializer):
    """ Serializer from ingredients """
    name = serializers.CharField(max_length=100)

    class Meta:
        model = models.Ingredient
        fields = ('id', 'name')

    def create(self, validated_data):
        """ create and return new ingredient """
        ingredients = models.Ingredient.objects.create(
            name=validated_data['name'],
        )

        return ingredients