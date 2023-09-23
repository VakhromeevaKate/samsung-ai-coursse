#Ответ: 0 (мы меняем индекс, а не элемент массива)

# Точка и область
#На координатной плоскости заданы две области:
#прямоугольник со сторонами параллельными осям координат,
#окружность с центром в начале координат.

#Определите, принадлежит ли данная точка объединению или пересечению областей. Если точка лежит на границе итоговой области, то считается, что она принадлежит ей.

#Формат входных данных:
#В единственной строке через пробел перечислены вещественные числа  x y x1 y1 x2 y2 r s.

#x, y – координаты точки
#x1, y1 – координаты левой нижней вершины прямоугольника
#x2, y2 – координаты правой верхней вершины прямоугольника
#r – радиус окружности 
#s – 0 или 1; где 0 – объединение, 1 – пересечение. 

#Формат выходных данных:
#В единственной строке необходимо вывести True, если точка принадлежит итоговой области, и False в противном случае.

dataInput = input()
dataList = dataInput.split(' ')

x = float(dataList[0])
y = float(dataList[1])
x1 = float(dataList[2])
y1 = float(dataList[3])
x2 = float(dataList[4])
y2 = float(dataList[5])
r = float(dataList[6])
s = float(dataList[7])

isInSquare = x >= x1 and x <= x2 and y >= y1 and y <= y2

isInCircle = x**2 + y**2 <= r**2

def CircleIntersectRect(x1, y1, x2, y2, x, y, r):
    if y < y1:   # Если центр сверху
        if x < x1: # Если центр в левом углу
            return ((x-x1)*(x-x1) + (y-y1)*(y-y1)) <= r*r
        if x > x2:          #Если центр в правом углу
            return ((x-x2)*(x-x2) + (y-y1)*(y-y1)) <= r*r
        return (y1-y) <= r #Если центр посередине
    if y > y2:   #Если центр снизу
        if x < x1:         #Если центр в левом углу
            return ((x-x1)*(x-x1) + (y-y2)*(y-y2)) <= r*r;
        if x > x2:          #Если центр в правом углу
            return ((x-x2)*(x-x2) + (y-y2)*(y-y2)) <= r*r;
        return (y-y2) <= r #Если центр посередине
    if x < x1:   #Если центр слева
        return (x1-x) <= r
    if x > x2:   #Если центр справа
        return (x-x2) <= r
    return True #Если внутри

def result():
    if s == 1:
        return isInCircle and isInSquare
    if s == 0:
        return (isInCircle or isInSquare) and CircleIntersectRect(x1, y1, x2, y2, 0, 0, r)
print(result())

print("CircleIntersectRect:" + str(CircleIntersectRect(x1, y1, x2, y2, 0, 0, r)))
print("isInSquare:" + str(isInSquare))
print("isInCircle:" + str(isInCircle))

# -1 -4 -1 -4 2 -2 2 0