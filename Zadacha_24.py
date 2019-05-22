str = input()
val = 0
for i in range(0,len(str)):
    if 'f' in i:
        val = val + 1
    else:
        print(-1)
if val == 2:
    print(3)


