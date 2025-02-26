# ЗАДАНИЕ ПО ТЕМЕ "Позиционирование в файле"

def custom_write(file_name, strings):
    strings_positions = {}
    name = file_name
    for i in range(len(strings)):
        file = open(name, 'a', encoding='utf-8')
        key = (i + 1, file.tell())
        file.write(f'{strings[i]}\n')
        strings_positions[key] = strings[i]
        file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)