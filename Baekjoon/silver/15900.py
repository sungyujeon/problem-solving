# 백준 15900번 S1
# 나무 탈출

# def arrange_tmps_to_parents(tmp_list):
#     global parents

#     while tmp_list:
#         a, b = tmp_list.pop()
        
#         if a == 1:
#             parents[b] = 1
#         elif b == 1:
#             parents[a] = 1
#         else:
#             if parents[a]:
#                 parents[b] = a
#             elif parents[b]:
#                 parents[a] = b
#             else:
#                 print('여기도 없다고?')

from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())

# tmp = []
# dp = [0] * (n+1)
# parents = [0] * (n+1)
# parents_set = set([1])

node_dict = {}
for i in range(1, n+1):
    node_dict[i] = []

for _ in range(n-1):
    a, b = map(int, input().split())
    
    node_dict[a].append(b)
    node_dict[b].append(a)
    
    
    # if a == 1:
    #     parents[b] = 1
    #     dp[b] = 1
    # elif b == 1:
    #     parents[a] = 1
    #     dp[a] = 1
    # else:
    #     if parents[a]:
    #         parents[b] = a
    #         parents_set.add(a)
    #     elif parents[b]:
    #         parents[a] = b
    #         parents_set.add(b)
        # else:
        #     tmp.append((a, b))

# if tmp:
#     arrange_tmps_to_parents(tmp)
# parents_set = set(parents)
cnt = 0
q = deque([[1]])
visited = [False] * (n+1)
depth = 0
while q:
    nodes = q.pop()

    tmp_nodes = []
    while nodes:
        node = nodes.pop()
        
        if not visited[node]:
            visited[node] = True
            
            child_nodes = node_dict[node]
            l = len(child_nodes)
            if l > 1 or node == 1:  # 자식이 있으면
                tmp_nodes.extend(child_nodes)
            else:  # leaf node이면
                cnt += depth
    depth += 1
    if tmp_nodes:
        q.append(tmp_nodes)

# for i in range(n, 1, -1):
#     if i not in parents_set:  # leaf node만 검사
#         child = i
#         pa = parents[i]  # leaf 노드의 부모 pa
        
#         dp_cnt = 1
#         while pa != 1:
#             dp_pa = dp[pa]
#             if dp_pa:
#                 dp_cnt += dp_pa
#                 dp[child] = dp_pa + 1
#                 break
#             else:
#                 child = pa
#                 pa = parents[child]
#                 dp_cnt += 1
#         cnt += dp_cnt
# print(f'dp:{dp}')
# print(f'cnt:{cnt}')

if cnt % 2:
    print('Yes')
else:
    print('No')
    
    