# 백준 1068번 S1
# 트리
# sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
del_node = int(input())

root = 0
dic = {}
for i in range(n):
    dic[i] = set()

for i in range(n):
    num = li[i]
    if num == -1:
        root = i
    else:
        if num != del_node and i != del_node:
            dic[num].add(i)
    

stack = [root]

cnt = 0
if del_node != root:
    while stack:
        node = stack.pop()
        child_nodes = dic[node]

        # del_node면 continue
        if node == del_node:
            continue
        
        # child_nodes가 없으면 cnt++
        if not child_nodes:
            cnt += 1
        else:  # child_nodes가 있으면
            stack.extend(child_nodes)
print(cnt)