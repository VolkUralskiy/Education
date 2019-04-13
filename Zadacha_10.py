import math
num = int(input())
num = math.fabs(num)

count = 1
num = num // 10

while num > 0:
    num //= 10
    count += 1


print(count)

