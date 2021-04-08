# 백준 9019번 G5
# DSLR
# sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs():
    q = deque()
    q.append([A, ''])
    visited[A] = 1
    while q:
        x, y = q.popleft()
        if x == B:
            print(y)
        D = x*2 % 10000
        if not visited[D]:
            visited[D] = 1
            q.append([D, y + 'D'])
        S = x - 1 if x != 0 else 9999
        if not visited[S]:
            visited[S] = 1
            q.append([S, y + 'S'])
        L = x % 1000 * 10 + x // 1000
        if not visited[L]:
            visited[L] = 1
            q.append([L, y + 'L'])
        R = x % 10 * 1000 + x // 10
        if not visited[R]:
            visited[R] = 1
            q.append([R, y + 'R'])

T = int(input())
for _ in range(T):
    A, B = map(int, input().split(' '))
    visited = [0] * 10000
    bfs()



# from collections import deque
# import sys
# input = sys.stdin.readline

# def d(num):
#     num *= 2
#     if num > 9999:
#         num %= 10000
#     return num

# def s(num):
#     if num == 0:
#         num = 9999
#     else:
#         num -= 1
#     return num


# def l(num):
#     num = (num % 1000) * 10 + (num // 1000)

#     return num


# def r(num):
#     num = (num % 10) * 1000 + (num // 10)

#     return num


# def bfs(_a, _b):
#     q = deque([[_a, '']])
#     visited = [False] * 10000

#     while q:
#         node, command = q.popleft()
            
#         if not visited[node]:
#             visited[node] = True
            
#             if node == b:
#                 return command
#             else:
#                 d_node, s_node, l_node, r_node = d(node), s(node), l(node), r(node)
#                 d_command, s_command, l_command, r_command = command + 'D', command + 'S', command + 'L', command + 'R'

#                 q.extend([[d_node, d_command], [s_node, s_command], [l_node, l_command], [r_node, r_command]])

        


# T = int(input())

for _ in range(T):
    # inputs
    a, b = map(int, input().split())

    # exec
    res = bfs(a, b)

    print(res)