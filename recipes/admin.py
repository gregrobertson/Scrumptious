from django.contrib import admin
from recipes.models import Recipe, Measure, FoodItem, Ingredient

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    pass


class MeasureAdmin(admin.ModelAdmin):
    pass


class FoodItemAdmin(admin.ModelAdmin):
    pass


class IngredientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Measure, MeasureAdmin)
admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Ingredient, IngredientAdmin)
