with open(r'files\example_write.txt', 'a', encoding='utf-8') as file:
    file.write("\nПривет мир!\n")
    file.write("Еще 1 строка.\n")

line_list = ['Если б мишки были пчелами,',
             'То они бы нипочем',
             'Никогда и не подумали',
             'Так высоко строить дом;',
             '',
             'И тогда (конечно, если бы',
             'Пчелы - это были мишки!)',
             'Нам бы, мишкам, было незачем',
             'Лазить на такие вышки!']

with open(r'files\example_write_02.txt', 'a', encoding='utf-8') as file:
    file.write('\n')
    for line in line_list:
        file.write(f'{line}\n')
