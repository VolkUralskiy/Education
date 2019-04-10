num = int(input())
if num < 0:
    mod_num = num * (-1)
    number = mod_num % 10
else:
     number = num % 10

print(number)