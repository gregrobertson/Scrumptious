from django import template

register = template.Library()


def resize_to(ingredient, target):
    serving = ingredient.recipe.servings
    amount = ingredient.amount
    if serving is not None and target is not None:
        try:
            ratio = int(target) / int(serving)
            return ratio * amount
        except ValueError:
            pass
    return amount


register.filter(resize_to)
