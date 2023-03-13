boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort()
girls.sort()
if len(boys) != len(girls):
    print('Количество мальчиков и девочек разное, '
          'кто-то может остаться без пары, знакомить не будем.')
else:
    for unity_b, unity_g in zip(boys, girls):
        print(f'{unity_b} и {unity_g}')
