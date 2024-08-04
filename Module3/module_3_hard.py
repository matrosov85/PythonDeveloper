# Дополнительное практическое задание по модулю "Подробнее о функциях"

# Написать функцию, подсчитывающую сумму всех чисел и длин всех строк в каждой внутренней структуре
def calculate_structure_sum(structure):
    summ = 0
    if isinstance(structure, (list, set, tuple)):
        for data in structure:
            summ += calculate_structure_sum(data)
    elif isinstance(structure, dict):
        summ += calculate_structure_sum(list(structure.items()))
    elif isinstance(structure, int):
        return structure
    elif isinstance(structure, str):
        return len(structure)
    return summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
