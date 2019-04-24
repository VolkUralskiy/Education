val = int(input())
for i in range(2, val):
    if val % i != 0:
       print('It not prime number')
    else:
        print("It is prime number")