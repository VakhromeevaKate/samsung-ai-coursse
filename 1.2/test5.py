import sys
import numpy as np
matrix = np.loadtxt(sys.stdin, delimiter=" ")

a = np.array(matrix, float)
mean_arr = 0 # среднee арифметическое по строкам
b = np.zeros(a.shape)

if len(a.shape) > 1:
    mean_arr = np.mean(a, axis=1)
    for i in range(a.shape[0]):
        b[i] = a[i] - mean_arr[i]
elif len(a.shape) > 0:
    mean_arr = np.mean(a)
    for i in range(len(a)):
        b[i] = a[i] - mean_arr
else:
    mean_arr = a
    b = a - mean_arr

print(str(b))
