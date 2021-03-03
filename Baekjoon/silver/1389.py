# 백준 1389번 S1
# 케빈 베이컨의 6단계 법칙
import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dfs(v):
    q = deque()
    q.append(v)
    q.append(True)

    cnt = 0
    depth = 1
    visited = [v]
    while q:
        person = q.popleft()

        if person is True:
            depth += 1
            q.append(True)
        else:
            knows = people_dict[person]
            for i in knows:
                if i not in visited:
                    visited.append(i)
                    q.append(i)
                    cnt += depth
            
            if len(visited) == n:
                return cnt
    
    return cnt
            

n, m = map(int, input().split())

# 사람 set 생성
people_dict = {}
for i in range(1, n+1):
    people_dict[i] = set()

for _ in range(m):
    a, b = map(int, input().split())
    people_dict[a].add(b)
    people_dict[b].add(a)

result_list = []
for i in range(1, n+1):
    result_list.append(dfs(i))

result = min(result_list)
result = result_list.index(result) + 1

print(result)