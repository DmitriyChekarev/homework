my_dict = {'Dmitry': 1991, 'Alexey': 1992, 'Sergey': 1993}
print(my_dict)
print(my_dict['Dmitry'])
print(my_dict.get('Vitalya'))
my_dict.update({'Victor': 1994,
                'Alexander': 1995})
print(my_dict)
del my_dict['Sergey']
print(my_dict)

my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко', 42.314}
print(my_set)
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.remove(1)
print(my_set)