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

def recipes(request, name):
    other_recipies = [x for x in list(DATA.keys()) if x != name]
    if name in DATA:
        data = DATA[name]
        servings = int(request.GET.get('servings', 1))
        servings_dict = list(range(1,11))
        servings_dict.remove(servings)
        if servings != 1:
            ing_dict = dict()
            for ingredient, amount in data.items():
                new_value = amount * servings
                ing_dict[ingredient] = new_value
            context = {
                'name': name,
                'recipe': ing_dict,
                'servings': servings,
                'other_recipies': other_recipies,
                'servings_dict': servings_dict,
            }
        else:
            context = {
                'name': name,
                'recipe': data,
                'servings': servings,
                'other_recipies': other_recipies,
                'servings_dict': servings_dict,
            }
    else:
        context = None
    return render(request, template_name='calculator/index.html', context=context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
