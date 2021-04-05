# 백준 14425번 S3
# 문자열 집합

import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

dic = {}
for _ in range(n):
    s = input()
    dic[s] = True

cnt = 0
for _ in range(m):
    s = input()

    if s in dic.keys():
        cnt += 1
print(cnt)

# 사전형으로 'a' ~ 'z' 까지 key 값 만들어서 list 찾기(시간 오래 걸림)
# dic = {}

# for i in range(26):
#     dic[chr(i+97)] = []

# for _ in range(n):
#     s = input()
#     dic[s[0]].append(s)

# cnt = 0
# for _ in range(m):
#     s = input()
#     if s in dic.get(s[0]):
#         cnt += 1

# print(cnt)


# dictionary 구조로 찾기(출력 초과)
# dic = {}
# for _ in range(n):
#     s = input()
#     dic[s] = 1

# cnt = 0
# for _ in range(m):
#     s = input()
#     res = dic.get(s)
#     print(res)

#     if res is not None:
#         cnt += 1

# print(cnt)