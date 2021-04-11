# 백준 11203번 S5
# numbers on a tree

import sys
input = sys.stdin.readline

_input = input().split()
l = len(_input)
num = int(_input[0])
root = 2 ** (num+1) - 1

if l == 1:
    print(root)
else:
    com = _input[1]
    
    idx = 1
    for d in com:
        if d == 'L':  # L라면
            idx *= 2        
        else:  # R라면
            idx = idx * 2 + 1
    
    res = (root + 1) - idx

    print(res)
    
    
    