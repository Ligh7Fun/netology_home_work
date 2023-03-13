# Задайте первоначальные значения

salary = 100000  # Заработная плата
percent_mortgage = 30  # Ипотека
percent_life = 50  # На жизнь

# Напишите свой код здесь
# без магических чисел
# 100 %
percent = 100
# месяцев в году
months_per_year = 12
# ипотека в месяц
mortgage_months = salary * percent_mortgage / percent
# ипотека в год
mortgage = mortgage_months * months_per_year
# затраты на жизнь
life = salary * percent_life / percent
# накопления за год
result = (salary - mortgage_months - life) * months_per_year

print('Ипотека:', mortgage)
print('Накопления:', result)
