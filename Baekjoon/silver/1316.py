# 백준 1316번 S5
# 그룹단어 체커

import sys

input = sys.stdin.readline

def group_word(_word):
    tmp = []
    for i in _word:
        if i not in tmp:
            tmp.append(i)
        else:
            if i == tmp[-1]:
                continue
            else:
                return 0
    return 1


n = int(input())

words = []
for _ in range(n):
    words.append(input())

result = 0
for word in words:
    result += group_word(word)
print(result)
    

