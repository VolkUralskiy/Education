num = int(input('3 символа\n'))
if num > 999:
    print('Ведите каректное значение')
else:
    num = num % 110 // 1
    print(num)