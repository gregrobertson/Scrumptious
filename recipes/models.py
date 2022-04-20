from django.db import models


# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)


class Ingredient(models.Model):
    amount = models.FloatField()
    recipe = models.ForeignKey(
        "recipe", related_name="ingredients", on_delete=models.CASCADE
    )
    measure = models.ForeignKey("measure", on_delete=models.PROTECT)
    food = models.ForeignKey("fooditem", on_delete=models.PROTECT)

    def __str__(self):
        return self.amount


class Step(models.Model):
    recipe = models.ForeignKey(
        "recipe", related_name="steps", on_delete=models.CASCADE
    )
    order = models.PositiveSmallIntegerField()
    directions = models.CharField(max_length=300)

    def __str__(self):
        return self.recipe
