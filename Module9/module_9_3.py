# Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка, которая высчитывает разницу длин строк из списков first и second, если их длины не равны
first_result = (len(string1) - len(string2) for string1, string2 in zip(first, second) if len(string1) != len(string2))

# Генераторная сборка, которая содержит результаты сравнения длин строк в одинаковых позициях из списков first и second
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))
