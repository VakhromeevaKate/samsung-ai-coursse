x = int(input())
y = int(input())

def isInInterval(x):
    return x >= 0 & x <= 2

if isInInterval(x) & isInInterval(y):
    print("Point HITS area")
else:
    print("Point is not in area")
