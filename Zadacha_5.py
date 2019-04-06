nuber = int(input())

A = ord('A')
Z = ord('Z')
a = ord('a')
z = ord('z')

if A <= nuber <= Z or a <= nuber <= z:
    print('Это буква', chr(nuber))
else:
    print('Это не буква, а символ', chr(nuber))

