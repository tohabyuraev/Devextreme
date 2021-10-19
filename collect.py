"""
Переводит C массивы в python подобные.
Сохранение в txt файле 'collect.txt'.
"""

import re


#  Шаблон на x, y со знаком '+' и '-'
pattern = re.compile(r'\{\d\.\d+f,\d\.\d+f')
pattern_ = re.compile(r'\{-\d\.\d+f,\d\.\d+f')

text = ''

results = re.findall(pattern, text)
results_ = re.findall(pattern_, text)

with open('collect.txt', 'w') as fout:
    fout.write('\n'.join(results_ + results))
