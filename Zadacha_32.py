a = int(input())
n = int(input())
i = 0
def power(a, n, i):
    a = a * a
    i += 1
    print(a)
    if n >= i:
        power(a, n, i)

power(a, n, i)

