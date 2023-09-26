#Нулевые столбцы
#Посчитайте число нулевых столбцов в матрице.

#Формат входных данных
#В первой и последующих строках вводится матрица построчно, числа в которой разделены пробелами.

#Формат выходных данных
#В единственной строке необходимо вывести целое число - количество нулевых столбцов данной матрицы.

#Для примера:

#Ввод	Результат
#0 0 0          2
#0 1 0

#Ответ:(штрафной режим: 0 %)

import sys
import numpy as np
matrix = np.loadtxt(sys.stdin, delimiter=" ")
mask = (matrix==0).all(axis=0).sum() #returns numpy.int64, but we need simple integer
count = int(mask.item())
#print(type(count))
print(str(count))