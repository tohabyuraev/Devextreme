import math

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic

from lebedev import (
    graph_5_11,
)


d_otn = 0.6
lambda_k = 2.0

print('Значение графика 5.11:')
print('должно быть ~ 0.019')
print(
    'на самом деле = ',
    graph_5_11(d_otn, lambda_k)
)

fig, ax = plt.subplots()

x = np.arange(0, 1, 0.001)
y = [graph_5_11(x, 2.0) for x in x]

ax.plot(x, y)

ax.set_xlim(0, 1.0)
ax.set_ylim(0, 0.04)

ax.xaxis.set_major_locator(tic.MultipleLocator(0.2))
ax.yaxis.set_major_locator(tic.MultipleLocator(0.01))
ax.grid(which='major', color='black')

plt.show()