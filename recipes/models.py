from django.db import models


# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=125, default="default name")
    author = models.CharField(max_length=100, default="default author")
    description = models.TextField(default="default description")
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
