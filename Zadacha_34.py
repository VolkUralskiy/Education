a = ['hello', 'hello', 'age', 'age', 'name']
b = 'hello'
c = 'age'
d = 'name'
val = 0
val_2 = 0
val_3 = 0
for i in range(0, 6):
    if i == b:
        val += 1
    if i == c:
        val_2 += 1
    if i == d:
        val_3 += 1
if val == 1:
    print(b)
if val_2 == 1:
    print(c)
if val_3 == 1:
        print(d)