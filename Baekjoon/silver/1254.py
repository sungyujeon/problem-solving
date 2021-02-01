# 백준 1254번 S1
# 팰린드롬 만들기


# 짧은 풀이
# s = input()
# n = len(s)
# for i in range(n):
#     if s[i:] == s[i:][::-1]:
#         print(n+i)
#         break;


import sys

s = sys.stdin.readline().strip()

def isPalindrome(word):
    while word:
        if word[0] == word[-1]:
            word = word[1:-1]
        else:
            return False
    return True

check_word = list(s)
result = list(s)
flag = 0
while True:
    if isPalindrome(check_word):
        break
    else:
        if len(check_word) == len(s):
            result.append(check_word.pop(0))
            flag -= 1
        else:
            result.insert(flag, check_word.pop(0))
            flag -= 1

print(len(result))
