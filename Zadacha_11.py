num_one = int(input())
num_two = int(input())

while num_one != 0 and num_two != 0:
    if num_one > num_two:
        num_one %= num_two
    else:
        num_two %= num_one

result = num_one + num_two
print(result)
