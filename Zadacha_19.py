x = int(input())
if x > 0:
    print('y', '=', x - 0,5)
elif x == 0:
    print('y', '=', 0)
elif x < 0:
    mod_x = x * (-1)
    print('y', '=', mod_x)