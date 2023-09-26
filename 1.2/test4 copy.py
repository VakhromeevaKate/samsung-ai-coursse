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
count = 0
matrix = np.loadtxt(sys.stdin)
mask = (matrix==0).all(axis=0) #returns boolean mask, but we need simple integer
for value in mask:
    if value == True:
        count += 1

print()
print(count)