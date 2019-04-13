value = input()
def Is_Palindrome(value):
    value_len = len(value)
    for i in range(value_len // 2):
         if value[i] != value[len(value) - 1 - i]:
             return 'not palindrom'
    return 'it is palindrom'

print(Is_Palindrome(value))