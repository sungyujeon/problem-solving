# 백준 5397번 S3
# 키로거

# 배열의 front, rear로 controll
# sys.stdin = open('input.txt', 'r')

import sys
from collections import deque
input = sys.stdin.readline

def func_input(c):
    global res, left, right

    if c in ['<', '>']:
        if c == '<':
            if left:
                right.appendleft(left.pop())
        else:
            if right:
                left.append(right.popleft())
    elif c == '-':
        if left:
            left.pop()
    else:
        left.append(c)

T = int(input())
for _ in range(T):
    li = list(input().rstrip())
    left, right = [], deque([])
    
    for char in li:
        func_input(char)
    
    res = ''.join(left) + ''.join(right)
    print(res)


