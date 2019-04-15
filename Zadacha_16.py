N = int(input())
for i in range(1, N):
    mod_num = 2 ** i
    if mod_num < N:
        print(i, mod_num)