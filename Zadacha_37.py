list = ['z', 'z', 'a', 's']
val = 0
val2 = 0
val3 = 0
for i in range(0, len(list) + 1):
    if i == 'z':
        val += 1
    elif i == 'a':
         val2 += 1
    elif i == 's':
         val3 += 1
 if val == 2:
     print('z')
 elif val2 == 2:
       print('a')
 elif  val3 == 2
     print('s')