"""
Разработать приложение для определения знака зодиака по дате рождения.

По информации с сайта https://calculat.ru/znak-zodiaka-po-date
21 марта — 20 апреля: Овен
21 апреля — 20 мая: Телец
21 мая — 21 июня: Близнецы
22 июня — 22 июля: Рак
23 июля — 23 августа: Лев
24 августа — 23 сентября: Дева
24 сентября — 23 октября: Весы
24 октября — 22 ноября: Скорпион
23 ноября — 21 декабря: Стрелец
22 декабря — 20 января: Козерог
21 января — 20 февраля: Водолей
21 февраля — 20 марта: Рыбы
"""
month = input('Введите месяц: ').lower()
day = int(input('Введите число: '))
"""
С тернарным оператором решение компактнее чем:

if month == 'январь':
    if (day <= 20):
        zodiac = 'Козерог'
    else 'Водолей'
"""
if month == 'январь':
    max_day = 31
    zodiac = 'Козерог' if (day <= 20) else 'Водолей'
elif month == 'февраль':
    # для февраля берем только 28 дней
    max_day = 28
    zodiac = 'Водолей' if (day <= 20) else 'Рыбы'
elif month == 'март':
    max_day = 31
    zodiac = 'Рыбы' if (day <= 20) else 'Овен'
elif month == 'апрель':
    max_day = 30
    zodiac = 'Овен' if (day <= 20) else 'Телец'
elif month == 'май':
    max_day = 31
    zodiac = 'Телец' if (day <= 20) else 'Близнецы'
elif month == 'июнь':
    max_day = 30
    zodiac = 'Близнецы' if (day <= 21) else 'Рак'
elif month == 'июль':
    max_day = 31
    zodiac = 'Рак' if (day <= 22) else 'Лев'
elif month == 'август':
    max_day = 31
    zodiac = 'Лев' if (day <= 23) else 'Дева'
elif month == 'сентябрь':
    max_day = 30
    zodiac = 'Дева' if (day <= 23) else 'Весы'
elif month == 'октябрь':
    max_day = 31
    zodiac = 'Весы' if (day <= 23) else 'Скорпион'
elif month == 'ноябрь':
    max_day = 30
    zodiac = 'Скорпион' if (day <= 22) else 'Стрелец'
elif month == 'декабрь':
    max_day = 31
    zodiac = 'Стрелец' if (day <= 21) else 'Козерог'
else:
    max_day = 0
    zodiac = ''

if not zodiac:
    print('Вы ошиблись при вводе данных, попробуйте снова.')
elif day < 1 or day > max_day:
    print(f'Вы указали месяц "{month}", числа '
          f'{day} в этом месяце нет, попробуйте снова.')
else:
    print(f'Ваш знак зодиака "{zodiac}"')
