import sys
from collections import deque
input = sys.stdin.readline

def isRight(li):
    stack = []
    for i in range(len(li)):
        c = li[i]
        
        if c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif c == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:  # 여는 것이면
            stack.append(c)

    if not stack:
        return True
    else:
        return False

def swap(li):
    left = li.popleft()
    li.append(left)
    return li

s = '[](){}'
list_s = deque(list(s))

cnt = 0
if isRight(list_s):
    cnt += 1

for _ in range(len(s)-1):
    if isRight(swap(list_s)):
        cnt += 1

print(cnt)