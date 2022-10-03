# x = 4
# print(x <= 10)
# if x <= 10:
#     print('je menší nebo rovno 10')
#     print('Další řádek')
#     if x < 5:
#         print('menší než 5')
# print('konec programu')

# x = 11
# if x <= 10:
#     print('je menší nebo rovno 10')
#     print('Další řádek')
# else:
#     print('něco jiného')
# print('konec programu')

# x = 4
# if x < 10 and x > 5:
#     print('je menší nebo rovno 10')
#     print('Další řádek')
# elif x < 5:
#     print('menší než 5')
# else:
#     print('něco jiného')
# print('konec programu')


# numbers = [1, 2, 3, 5, 5.5]
# print(numbers)
# print(numbers[:2])
# numbers.append(9999)
# print(numbers)
# numbers[0] = 8888
# print(numbers)
# numbers.reverse()
# numbers2 = numbers
# print(numbers2)

# print(sum(numbers))


# numbers2D = [
#     [1, 2, 3, 5, 5.5]
#     [11, 22, 343, 58, 5.5]
#     ]

#range_no = list(range(20, 100, 10))
# print(range_no)

# # Tuple
# numbers = (1, None, 'Petr', True, 5.5)
# print(numbers[0])
# # nejde modifikovat
# # numbers[0] = 8888
# # funkce list je přetypování
# numbers_list = list(numbers)
# numbers_list[0] = 888
# # přetypování zpátky na tuple
# numbers = tuple(numbers_list)
# print(numbers)

# Set
# my_set = {1, 1, 2, 3, 5, 5.5}
# print(my_set)
# names = ['Petr', 'Jirka', 'Katka', 'Katka']
# names = list(set(names))
# print(names)

# Dictionary
family = {
    'name': 'Petr',
    'age': 29,
    'sourozenci': [{
            'name': 'Gabriela',
            'age': 40,
    },
        {
        'name': 'Michal',
        'age': 20,
    }],
}
# print(family['name'])
print(family['sourozenci'][1]['name'])
print(family['sourozenci'][1]['age'])
