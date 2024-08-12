# Домашнее задание по теме "Позиционирование в файле"

def custom_write(file_name, strings):
    string_positions = {}
    string_number = 1
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        string_positions.update({(string_number, file.tell()): string})
        file.write(f'{string}\n')
        string_number += 1
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')