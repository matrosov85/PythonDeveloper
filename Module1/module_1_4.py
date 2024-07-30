# Практическое задание по теме "Организация программ и методы строк"

# Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
my_string = input()

# Вывести количество символов введённого текста
print(len(my_string))

# Выведите строку my_string в верхнем регистре.
print(my_string.upper())

# Выведите строку my_string в нижнем регистре.
print(my_string.lower())

# Измените строку my_string, удалив все пробелы.
my_string = my_string.replace(' ', '')

# Выведите первый символ строки my_string.
print(my_string[0])

# Выведите последний символ строки my_string.
print(my_string[-1])
