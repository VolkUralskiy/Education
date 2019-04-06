var = input('What to calculate? (m, p, V):')
if var == 'm':
    V = int(input())
    p = int(input())
    m = V * p
    print('масса = ', m,'кг')
elif var == 'p':
    V = int(input())
    m = int(input())
    p = m / V
    print('плотность -', p)
elif var == 'V':
    p = int(input())
    m = int(input())
    V = m / p
    print('объем -', V)