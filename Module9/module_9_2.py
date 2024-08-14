# Домашнее задание по теме "Списковые, словарные сборки"

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Список, созданный при помощи сборки, состоящий из длин строк списка first_strings, при условии, что длина строк не
# менее 5 символов
first_result = [len(string) for string in first_strings if len(string) > 4]

# Список, созданный при помощи сборки состоящий из пар слов одинаковой длины
second_result = [(first, second) for first in first_strings for second in second_strings if len(first) == len(second)]

# Словарь, созданный при помощи сборки, где парой ключ-значение является строка-длина строки если длина строки четная
third_result = {string: len(string) for string in first_strings + second_strings if not len(string) % 2}

print(first_result)
print(second_result)
print(third_result)
