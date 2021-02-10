# 백준 4153번 B3
# 직각삼각형

import sys

input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '0 0 0':
        break

    tri = list(map(int, s.split()))
    
    max_num = tri.pop(tri.index(max(tri)))
    w, h = tri.pop(), tri.pop()
    
    if w ** 2 + h ** 2 == max_num ** 2:
        print('right')
    else:
        print('wrong')