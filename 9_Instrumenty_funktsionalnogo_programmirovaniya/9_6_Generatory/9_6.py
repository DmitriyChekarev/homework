def all_variants(text):
    n = len(text)
    # Проходим по всем возможным длинам подпоследовательностей (от 1 до n)
    for length in range(1, n + 1):
        # Проходим по всем возможным начальным позициям
        for start in range(n):
            # Формируем подпоследовательность, начиная с текущей позиции и до конца строки
            if start + length <= n:
                yield text[start:start + length]

# Пример использования функции-генератора
a = all_variants("abc")
for i in a:
    print(i)