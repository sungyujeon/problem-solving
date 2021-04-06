# 백준 9372번 S3
# 상근이의 여행

# sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, e = map(int, input().split())
    
    dic = {}
    for i in range(1, n+1):
        dic[i] = set()

    for _ in range(e):
        a, b = map(int, input().split())

        dic[a].add(b)
        dic[b].add(a)
        
    visited = [False] * 1001
    stack = [1]
    visited[1] = True

    cnt = 0
    while stack:
        node = stack.pop()
        
        tmp_nodes = dic[node]
        while tmp_nodes:
            tmp_node = tmp_nodes.pop()
            
            if not visited[tmp_node]:
                visited[tmp_node] = True
                stack.append(tmp_node)
                cnt += 1
    
    print(cnt)
        