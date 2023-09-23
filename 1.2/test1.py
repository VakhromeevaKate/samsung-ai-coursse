#Заполните пропуски (a[1] и b[2]) так, чтобы данная программы вывела "0.0"

import numpy as np

a = np.array([5, -2, 3], float)

b = np.array([1, 1, -1], float)

print(np.dot(a, b))