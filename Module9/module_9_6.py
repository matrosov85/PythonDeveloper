# Домашнее задание по теме "Генераторы"

# Функция-генератор, принимающая строку и возвращающая объект-генератор,
# при каждой итерации которого возвращаются подпоследовательности переданной строки
def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text)-i):
            yield text[j:j+i+1]


a = all_variants("abc")
for i in a:
    print(i)
