from pprint import pprint


def get_cook_book(file_name: str) -> dict:
    """Функция для получения словаря из файла"""
    cook_book = {}
    with open(file_name, 'rt', encoding='utf-8') as f:
        for line in f:
            dish = line.strip()
            ingredients_count = int(f.readline())
            ingredients = []

            for _ in range(ingredients_count):
                temp = f.readline()
                ingredient_name, quantity, measure = temp.split(' | ')
                ingredient = {
                    'ingredient': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure.replace('\n', ''),
                }
                ingredients.append(ingredient)

            f.readline()
            cook_book[dish] = ingredients

    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    shop_list = {}
    cook_book = get_cook_book('recipes.txt')

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]

            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {
                        'measure': measure,
                        'quantity': quantity,
                    }

    return shop_list


if __name__ == "__main__":
    pprint(get_cook_book('recipes.txt'))
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
