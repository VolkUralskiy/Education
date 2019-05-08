F1 = 1
F2 = int(input())
i = int(input())
def Fibanachi(F2, i, F1):
    F1 = i + F1
    print(F1)
    if F1 <= F2:
        Fibanachi(F2, i, F1)