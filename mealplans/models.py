from django.db import models
from django.conf import settings

# Create your models here.

USER_MODEL = settings.AUTH_USER_MODEL


class MealPlan(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField(auto_now_add=False, null=True, blank=True)
    owner = models.ForeignKey(
        USER_MODEL,
        related_name="mealplans",
        on_delete=models.CASCADE,
        null=True,
    )
    recipes = models.ManyToManyField("recipes.Recipe", related_name="recipes")

    def __str__(self):
        return str(self.name) + " by " + str(self.owner)
