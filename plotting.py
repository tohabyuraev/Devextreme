import numpy as np
import matplotlib.pyplot as plt


from_file_1 = np.load('3_5_1_1.npz')
from_file_2 = np.load('3_5_1_2.npz')
from_file_3 = np.load('3_5_1_3.npz')
from_file_4 = np.load('3_5_1_4.npz')
from_file_5 = np.load('3_5_1_5.npz')

plt.plot(from_file_1['x'], from_file_1['y'])
plt.plot(from_file_2['x'], from_file_2['y'])
plt.plot(from_file_3['x'], from_file_3['y'])
plt.plot(from_file_4['x'], from_file_4['y'])
plt.plot(from_file_5['x'], from_file_5['y'])

from_file_1 = np.load('3_5_2_1.npz')
from_file_2 = np.load('3_5_2_2.npz')
from_file_3 = np.load('3_5_2_3.npz')
from_file_4 = np.load('3_5_2_4.npz')

plt.plot(from_file_1['x'], from_file_1['y'])
plt.plot(from_file_2['x'], from_file_2['y'])
plt.plot(from_file_3['x'], from_file_3['y'])
plt.plot(from_file_4['x'], from_file_4['y'])

from_file_1 = np.load('3_5_3_1.npz')
from_file_2 = np.load('3_5_3_2.npz')
from_file_3 = np.load('3_5_3_3.npz')
from_file_4 = np.load('3_5_3_4.npz')

plt.plot(from_file_1['x'], from_file_1['y'])
plt.plot(from_file_2['x'], from_file_2['y'])
plt.plot(from_file_3['x'], from_file_3['y'])
plt.plot(from_file_4['x'], from_file_4['y'])

from_file_1 = np.load('3_5_4_1.npz')
from_file_2 = np.load('3_5_4_2.npz')
from_file_3 = np.load('3_5_4_3.npz')
from_file_4 = np.load('3_5_4_4.npz')

plt.plot(from_file_1['x'], from_file_1['y'])
plt.plot(from_file_2['x'], from_file_2['y'])
plt.plot(from_file_3['x'], from_file_3['y'])
plt.plot(from_file_4['x'], from_file_4['y'])

plt.xlim(-3.5, 9.5)
plt.ylim(0, 0.035)

plt.xlabel(r'$\lambda_k \cdot \sqrt{M ^ 2 - 1}$')
plt.ylabel(r'$c ^ \alpha _{y1}$')

plt.grid()
plt.show()