"""
Сохраняет массивы из 'collect.txt' в форме numpy. 
"""

import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic


values = np.genfromtxt('3_5_4_4.txt', delimiter=',')

result_x = [value[0] for value in values]
result_y = [value[1] for value in values]

print(result_x)
print(result_y)

np.savez('3_5_4_4.npz', x=result_x, y=result_y)