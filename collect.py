"""
Переводит C массивы в python подобные.
Сохранение в txt файле 'collect.txt'.
"""

import re


#  Шаблон на x, y со знаком '+' и '-'
pattern_x = re.compile(r'\{(-?\d\.\d+)')
pattern_y = re.compile(r'(-?\d\.\d+)f\}')

text = '{{-0.00000f, 0.00000f}, {0.00940f, 0.01601f}, {1.00000f, 0.00000f}};'

result_x = pattern_x.findall(text)
result_y = pattern_y.findall(text)

with open('collect.txt', 'w') as fout:
    fout.write('x =\n')
    fout.write(',\n'.join(result_x))
    fout.write('\ny =\n')
    fout.write(',\n'.join(result_y))