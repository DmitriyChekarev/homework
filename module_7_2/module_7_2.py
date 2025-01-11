def custom_write(file_name, strings):
    dict_strings = {}
    strings_positions = 0
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        strings_positions += 1
        cursor = file.tell()
        dict_strings[(strings_positions, cursor)] = string
        file.write(string + '\n')
    file.close()
    return dict_strings

info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)