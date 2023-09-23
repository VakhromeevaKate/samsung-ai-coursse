dataInput = input()
dataList = dataInput.split(' ')

x1 = float(dataList[0])
y1 = float(dataList[1])
x2 = float(dataList[2])
y2 = float(dataList[3])
r = float(dataList[4])

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
print(CircleIntersectRect(x1, y1, x2, y2, 0, 0, r))
    
# -2 -2 -1 -1 1.3
# -1 -4 2 -2 2
