"""
Сохраняет массивы из csv-файлов в форме C-массивов.
"""
import os
import csv


#  Список всех файлов в директории
all_files = os.listdir()
#  Список всех csv-файлов в директории
csv_files = [
    file for file in all_files
    if file.endswith('.csv')
]

#  Запись имен csv-файлов
with open('convert.txt', 'w') as fout:
    fout.write('\n'.join(csv_files) + '\n\n')

#  Формирование C-массивов
for i, file in enumerate(csv_files):
    with open(file, 'r') as csv_file:
        data = list(csv.reader(csv_file))

    pattern = f'unsigned int Length_1_{i + 1} = {len(data)}; float Matrix_1_{i + 1}[][2] = {{'
    for x, y, _ in data:
        pattern += '{{{:.5f}f, {:.5f}f}}, '.format(
            float(x),
            float(y),
        )

    with open('convert.txt', 'a') as fout:
        fout.write(pattern[:-2] + '};' + '\n')