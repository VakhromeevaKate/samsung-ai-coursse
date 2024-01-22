import sys
import numpy as np
matrix = [[float(i) for i in line.split()] for line in sys.stdin]
matrix = np.array(matrix)

a = matrix - matrix.mean(1, keepdims=True)

print(a)