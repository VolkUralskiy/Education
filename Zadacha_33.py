a = int(input())
i = 0
def Razvorot(a, i):
    print(a)
    a -= 1
    if a >= i:
       Razvorot(a, i)
Razvorot(a, i)

