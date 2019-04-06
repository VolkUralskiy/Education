symbol = input('kb or b \n')
number = int(input('Ведите число \n'))
if symbol == 'kb' or symbol == 'KB' or symbol == 'kB' or symbol == 'Kb':
    translation = number / 1024
    print(round(translation, 3), 'B')
elif symbol == 'b' or symbol == 'B':
    translation = number * 1024
    print(translation, 'KB')
else:
    print('Ведите каректное значение!!!')