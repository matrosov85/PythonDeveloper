# Домашнее задание по теме "Интроспекция"

# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию
# этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': obj.__class__.__module__
    }


number_info = introspection_info(42)
print(number_info)
