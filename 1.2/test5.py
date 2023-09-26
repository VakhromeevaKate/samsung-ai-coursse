import sys
import numpy as np
matrix = np.loadtxt(sys.stdin)

a = matrix - matrix.mean(1, keepdims=True)

print(a)