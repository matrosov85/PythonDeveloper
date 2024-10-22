# Домашнее задание по теме "Интроспекция"

# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию
# этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

def introspection_info(obj):
    attributes = []
    methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)
    return {
        'type': type(obj).__name__,
        'attributes': attributes,
        'methods': methods,
        'module': obj.__class__.__module__
    }


number_info = introspection_info(42)
print(number_info)
