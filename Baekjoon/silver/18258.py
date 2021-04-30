# 백준 18258 S4
# 큐2
# sys.stdin = open('input.txt')

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
for _ in range(n):
    command = input().split()
    
    if command[0] == 'push':
        cmd, num = command[0], command[1]
        dq.append(int(num))
    else:
        cmd = command[0]

        if cmd == 'pop':
            if dq:
                print(dq.popleft())
            else:
                print(-1) 
        elif cmd == 'size':
            print(len(dq))
        elif cmd == 'empty':
            if dq:
                print(0)
            else:
                print(1)
        elif cmd == 'front':
            if dq:
                print(dq[0])
            else:
                print(-1)
        elif cmd == 'back':
            if dq:
                print(dq[-1])
            else:
                print(-1)   
