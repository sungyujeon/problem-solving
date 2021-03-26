# 백준 16953번 S1
# A -> B
import sys
from collections import deque
# input = sys.stdin.readline

def bfs(_a, _b):
    depth = 1
    _q = deque()
    _q.append(_a)
    stack = [_q]

    while stack:
        q = stack.pop()
        depth += 1

        tmp_q = deque()
        for i in range(len(q)):
            num = q.popleft()

            n1 = num * 2
            n2 = int(str(num) + '1')
            
            if i == 0 and n1 > _b:
                return -1
            
            if n1 == _b or n2 == _b:  # 같은 값이 나오면
                return depth
            
            if n1 < _b:
                tmp_q.append(n1)
            if n2 < _b:
                tmp_q.append(n2)
        
        if tmp_q:
            stack.append(tmp_q)


a, b = map(int, input().split())

res = bfs(a, b)
print(res)