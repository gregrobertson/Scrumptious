from tkinter import CASCADE
from django.db import models
from django.conf import settings

# Create your models here.

USER_MODEL = settings.AUTH_USER_MODEL


class MealPlan(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(USER_MODEL, on_delete=CASCADE)
    recipes = models.ManyToManyField("recipes.Recipe", related_name="recipes")
