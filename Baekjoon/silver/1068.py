# 백준 1068번 S1
# 트리

# dict >> 0~(n-1) 배열
# 삭제 idx의 value stack에 넣고 False로 변경
# stack에 들어가있는 idx의 value stack에 넣고 False 반복

import sys

input = sys.stdin.readline

n = int(input())
nodes = list(map(int, input().split()))
del_idx = int(input())

cnt = 0
if del_idx != 0:
    node_dict = {}
    for i in range(n):
        node_dict[i] = []

    for i in range(1, n):
        node_dict[nodes[i]].append(i)

    stack = [del_idx]

    while stack:
        idx = stack.pop()

        while node_dict[idx]:
            stack.append(node_dict[idx].pop())
        node_dict[idx] = False

    # idx == 0 제외하고 False가 아니고 빈 배열도 아닌 것
    for i in range(1, n):
        check = node_dict[i]
        if check != False and check == []:
            cnt += 1

    if cnt == 0:
        cnt = 1

print(cnt)