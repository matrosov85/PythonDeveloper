# Домашнее задание по теме "Введение в функциональное программирование"

# Функция, возвращающая словарь, где ключ - название вызванной функции, а значением - результат её работы
def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results.update({function.__name__: function(int_list)})
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
