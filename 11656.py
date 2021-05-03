# 백준 11656번 S4
# 접미사 배열

import sys
input = sys.stdin.readline

s = input().rstrip()

s_set = set()

for i in range(len(s)):
    tmp = s[i:]
    s_set.add(tmp)

s_list = list(s_set)
s_list.sort()

for i in range(len(s_list)):
    print(s_list[i])


