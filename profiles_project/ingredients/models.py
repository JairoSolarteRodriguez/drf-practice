from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def create(self, name):
        """ Create new ingredient """
        ingredient = self.model(name=name)

        ingredient.save(using=self._db)

        return ingredient
