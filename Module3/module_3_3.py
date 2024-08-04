# Домашняя работа по уроку "Распаковка позиционных параметров"

# Создайте функцию print_params, которая принимает три параметра со значениями по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Создайте список values_list с тремя элементами разных типов
values_list = ['fsd', 2.5]

# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
values_dict = {'c': 25}

# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров
print_params(*values_list, **values_dict)

# Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = [54.32, 'Строка']

# Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
