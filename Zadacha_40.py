f_line = [1, 2, 4, 5, 6]
s_line = [1, 2, 7, 5, 6]
m = 0
o = 0
for i,j in enumerate(range(0,6)):
    val_f = f_line[i]
    val_s = s_line[i]
    if val_f == val_s:
        m += 1
    else:
        o += 1
if m > o:
    print('Списки совпадают')
elif m < o:
    print('Списки имеют разные значения')