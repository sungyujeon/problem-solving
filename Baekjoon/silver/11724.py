# 백준 11724번 S2
# 연결 요소의 개수

# visited에 넣고 graph_dict 모두 돌면서 cnt

import sys

input = sys.stdin.readline


def dfs(_dict, start):
    visited = set()
    stack = [start]

    while stack:
        num = stack.pop()
        if num not in visited:
            visited.add(num)
            stack.extend(_dict[num])

    return visited

n, m = map(int, input().split())

g_dict = {}
# g_dict 빈 배열 초기화
for i in range(1, n+1):
    g_dict[i] = []

# g_dict, 연결 요소 할당
for i in range(m):
    a, b = map(int, input().split())
    
    # 데이터 넣기
    g_dict[a].append(b)
    g_dict[b].append(a)


cnt = 0
global_visited = set()
for i in g_dict:  # i -> key 돌면서
    if i not in global_visited:
        global_visited = global_visited | dfs(g_dict, i)
        cnt += 1

print(cnt)

