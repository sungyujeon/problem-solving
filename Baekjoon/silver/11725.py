# 백준 11725번 S2
# 트리의 부모 찾기

import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

n = int(input())

dic = {}
for i in range(1, n+1):
    dic[i] = set()

for _ in range(n-1):
    a, b = map(int, input().split())
    
    dic[a].add(b)
    dic[b].add(a)

tree = [0] * (n + 1)
visited = [False] * 100001
stack = [1]

while stack:
    node = stack.pop()
    visited[node] = True

    child_nodes = dic[node]
    while child_nodes:
        tmp_node = child_nodes.pop()
        if not visited[tmp_node]:
            visited[tmp_node] = True
            stack.append(tmp_node)
            tree[tmp_node] = node

for i in range(2, n+1):
    print(tree[i])
                

# 틀림 왜 틀렸지...?
# dic = {}
# for i in range(1, n+1):
#     dic[i] = set()

# tree = [0] * (n + 1)
# for _ in range(n-1):
#     a, b = map(int, input().split())
    
#     dic[a].add(b)
#     dic[b].add(a)

# for k in dic.keys():
#     values = dic[k]
#     for value in values:
#         if value == 1:
#             tree[k] = 1
#         elif tree[value] == 0:
#             tree[value] = k
#         elif tree[k] != 0 and tree[value] != 0:
#             pass
#         else:
#             tree[k] = value

# for i in range(2, n+1):
#     print(tree[i])





# li1 = []
# li2 = []

# tree = [0] * (n + 1)
# for _ in range(n):
#     a, b = map(int, input().split())

#     li1.append((a, b))
#     li2.append((b, a))

# li1.sort(key=lambda x: (x[0], x[1]))
# li2.sort(key=lambda x: (x[0], x[1]))
