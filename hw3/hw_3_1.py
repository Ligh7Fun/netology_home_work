boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    print('Количество мальчиков и девочек разное, '
          'кто-то может остаться без пары, знакомить не будем.')
else:
    boys.sort()
    girls.sort()
    # либо если длины списков равны, отдельно создать список
    # pairs = list(zip(sorted(boys), sorted(girls)))
    # и итерироваться по данному списку
    for boy, girl in zip(boys, girls):
        print(f'{boy} и {girl}')
