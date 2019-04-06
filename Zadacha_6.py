import math
# start_nam = int(input())
# finish_nam = int(input())
# for i in range(start_nam, finish_nam):
#     if i % 2 == 0:
#         print(i)

# str_value = "Георгий"
#
# # for i in str_value:
# #     print(i)
#
# num = 0
#
# while num < 10:
#     num += 1
#     if num % 2 == 0:
#         print(num






ferst_nam = int(input())
sekond_nam = int(input())
thierd_nam = int(input())
D = math.pow(sekond_nam, 2) - 4 * ferst_nam * thierd_nam
D_sekond = math.pow(ferst_nam, 2) - 4 * sekond_nam * thierd_nam
D_thierd = math.pow(thierd_nam, 2) - 4 * sekond_nam * ferst_nam
print(D, D_sekond, D_thierd)

