from django.shortcuts import render
from django.http import HttpResponse


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
}


def dishes(request, recipe):

    if recipe in DATA.keys():
        portions = request.GET.get('portions', 1)
        ingredients = {}
        for ingredient in DATA[recipe]:
            ingredients[ingredient] = round(DATA[recipe][ingredient] * int(portions), 2)
        context = {
            'recipe': ingredients
        }
    else:
        context = {}
    return render(request, 'calculator/index.html', context)
