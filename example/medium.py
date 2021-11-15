import math

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic

from lebedev import (
    graph_3_2,
)


M = math.sqrt(2.44)
lambda_n = 1.0
lambda_c = 1.0

print('Значение графика 3.2:')
print('должно быть ~ 0.5')
print(
    'на самом деле = ',
    graph_3_2(M, lambda_n, lambda_c)
)