list = {0, 1, 2, 3, 4, 5}
def list_f(list):
    for i in range(0, len(list) + 1):
        if i % 2 == 0:
            print(i)
list.sort(list_f(list))