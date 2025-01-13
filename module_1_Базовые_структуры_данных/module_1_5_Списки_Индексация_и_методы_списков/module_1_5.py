food = ['apple', 'coconut', 'banana']

food.append(True)
print(food)

food.extend('string') # 's', 't', 'r', 'i', 'n', 'g'
food.extend(['string', 2]) # 'string', 2
print(food)

food.remove('apple')
print(food)

print('coconut' not in food)

print(food[0:3:1])