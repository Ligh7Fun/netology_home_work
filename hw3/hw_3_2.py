cook_book = [
    ['салат',
        [
            ['картофель', 100, 'гр.'],
            ['морковь', 50, 'гр.'],
            ['огурцы', 50, 'гр.'],
            ['горошек', 30, 'гр.'],
            ['майонез', 70, 'мл.'],
        ]
     ],
    ['пицца',
        [
            ['сыр', 50, 'гр.'],
            ['томаты', 50, 'гр.'],
            ['тесто', 100, 'гр.'],
            ['бекон', 30, 'гр.'],
            ['колбаса', 30, 'гр.'],
            ['грибы', 20, 'гр.'],
        ],
     ],
    ['фруктовый десерт',
        [
            ['хурма', 60, 'гр.'],
            ['киви', 60, 'гр.'],
            ['творог', 60, 'гр.'],
            ['сахар', 10, 'гр.'],
            ['мед', 50, 'мл.'],
        ]
     ]
]
person = 5

for dish, ingredients in cook_book:
    print(f'{dish.capitalize()}:')
    for ingredient, quantity, unit in ingredients:
        print(f'{ingredient}, {quantity * person}{unit}')
    print()

# второй вариант, немного помучать себя и всех кто это будет читать :)
# for dish in range(len(cook_book)):
#     print(f'{cook_book[dish][0].capitalize()}:')
#     for ingredients in range(len(cook_book[dish][1])):
#         print(f'{cook_book[dish][1][ingredients][0]}, '
#               f'{cook_book[dish][1][ingredients][1] * person}'
#               f'{cook_book[dish][1][ingredients][2]}')
#     print()
