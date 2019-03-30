temporal = input("Укажите температуру:")
sign = temporal[-1]
result = int(temporal[0:-1])
if sign == 'F' or sign == 'f':
    result = round(result * (9/5) + 32,2)
    print(str(result) + 'C')
elif sign == 'C' or 'c':
    result = round(result - 32 * (5/9),2)
    print(str(result) + 'F')