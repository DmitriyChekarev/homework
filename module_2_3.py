my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a1 = 0

while a1 < len(my_list):
    a2 = my_list[a1]
    a1 = a1 + 1
    if a2 == 0:
        continue
    elif a2 < 0:
        break
    else:
        print(a2)