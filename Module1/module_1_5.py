# Практическое задание по теме "Неизменяемые и изменяемые объекты. Кортежи и списки"

# Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var = (25, 'python', True, 4.85, [5, 6, 7])

# Выполните операции вывода кортежа immutable_var на экран.
print('Immutable tuple:', immutable_var)

#  Попытайтесь изменить элементы кортежа immutable_var.
# immutable_var[2] = False

# Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list = [4, 8.5, True, 'fsd']

# Измените элементы списка mutable_list.
mutable_list[2] = False

# Выведите на экран измененный список mutable_list.
print('Mutable list:', mutable_list)