# 백준 5567번 S1
# 결혼식

# sys.stdin = open('input.txt', 'r')
# from pprint import pprint
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    global N, graphs

    visited = [False] * (N+1)
    visited[start] = True
    q = deque([start])
    cnt = 0

    while q:
        person = q.popleft()
        
        for p in graphs[person]:
            if not visited[p]:
                visited[p] = True
                if person == 1:
                    q.append(p)
                cnt += 1

    return cnt

N = int(input())
M = int(input())
graphs = [[] for _ in range(N+1)]
for _ in range(M):
    f1, f2 = map(int, input().split())
    graphs[f1].append(f2)
    graphs[f2].append(f1)

res = bfs(1)
print(res)