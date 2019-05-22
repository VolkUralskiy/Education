x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
def distance(x1, y1, x2, y2):
    if x1 > y1:
        c = x1 - y1
    elif x1 < y1:
        c = y1 - x1
    if x2 > y2:
        f = x2 - y2
    elif x2 < y2:
        f = y2 - x2
    print(c)
    print(f)
distance(x1, y1, x2, y2)