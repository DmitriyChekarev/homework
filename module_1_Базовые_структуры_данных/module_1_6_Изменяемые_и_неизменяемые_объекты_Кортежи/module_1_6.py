immutable_var = ("Dmitry", True, 777, 77.77)
print(immutable_var)
print(type(immutable_var))

print("Dmitry" not in immutable_var)
#Кортежи очень похожи на списки, но имеют одно важное отличие — они неизменяемые.

mutable_list = ["Dmitry", True, 777, 77.77]
print("Dmitry" in mutable_list)
mutable_list[0] = 'Alex'
mutable_list.remove(True)
mutable_list.extend(["Den"])
mutable_list.append(True)
print(mutable_list)