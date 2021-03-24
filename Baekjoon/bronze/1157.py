# 백준 1157번 B1
# 단어 공부

import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

s = map(lambda x: x.upper(), list(input().rstrip()))


dic = {}
for c in s:
    char = dic.get(c)
    if char:
        dic[c] += 1
    else:
        dic[c] = 1

flag = False
max_value = 0
res = ''
for k, v in dic.items():
    if v > max_value:
        max_value = v
        res = k
        flag = False
    elif v == max_value:
        flag = True

if flag:
    print('?')
else:
    print(res.upper())


        
