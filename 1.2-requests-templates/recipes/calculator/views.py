from django.http import request
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request, servings=1):
    recipe = DATA['omlet']
    adjusted_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    context = {
        'recipe': adjusted_recipe,
    }
    return render(request, 'calculator/index.html', context)

def pasta(requests, servings=1):
    recipe = DATA['pasta']
    adjusted_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    context = {
        'recipe': adjusted_recipe,
    }
    return render(requests, 'calculator/index.html', context)

def buter(requests, servings=1):
    recipe = DATA['buter']
    adjusted_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    context = {
        'recipe': adjusted_recipe,
    }
    return render(requests, 'calculator/index.html', context)