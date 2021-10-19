import time

import numpy as np
import matplotlib.pyplot as plt


from_file_1 = np.load('3_5_1_1.npz')
from_file_2 = np.load('3_5_1_2.npz')
from_file_3 = np.load('3_5_1_3.npz')
from_file_4 = np.load('3_5_1_4.npz')
from_file_5 = np.load('3_5_1_5.npz')

start = time.time()

x_interp = np.arange(-3.5, 9.5, 1e-5)
y_interp = np.interp(
    x_interp,
    from_file_1['x'],
    from_file_1['y']
)
y_interp = np.interp(
    x_interp,
    from_file_2['x'],
    from_file_2['y']
)
y_interp = np.interp(
    x_interp,
    from_file_3['x'],
    from_file_3['y']
)
y_interp = np.interp(
    x_interp,
    from_file_4['x'],
    from_file_4['y']
)
y_interp = np.interp(
    x_interp,
    from_file_5['x'],
    from_file_5['y']
)

stop = time.time()

print(len(x_interp))

print(stop - start)