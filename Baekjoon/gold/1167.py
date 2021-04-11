# 백준 1167번 G3
# 트리의 지름

# sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline


def dfs(start, _childs, _result):
    for node, dist in _childs[start]:
        if _result[node] == 0:
            _result[node] = _result[start] + dist
            dfs(node, _childs, _result)


v = int(input())

# idx 값의 부모가 자식 노드 리스트 정보를 담은 childs 리스트
childs = [[] for _ in range(v+1)]
for _ in range(v):
    li = list(map(int, input().split()))
    parent = li[0]
    l = len(li)

    # 자식 노드들의 정보를 튜플 형태로 저장(child_node, distance)
    for i in range(1, l-1, 2):
        childs[parent].append((li[i], li[i+1]))


# 임의의 정점 start에서 child idx까지 가는 데 필요한 distance 리스트(result1)
result1 = [0] * (v+1)
dfs(1, childs, result1)
result1[1] = 0

# 임의의 정점으로부터 가장 거리가 먼 node 찾기
node1 = 0
tmp_max_dist = 0
for i in range(2, v+1):
    curr_dist = result1[i]
    if curr_dist > tmp_max_dist:
        tmp_max_dist = curr_dist
        node1 = i

# 임의의 정점으로부터 가장 거리가 먼 node로 부터 가장 거리가 먼 node 찾기
result2 = [0] * (v+1)
dfs(node1, childs, result2)
result2[node1] = 0

# (트리의 지름이 되는) node1으로부터 가장 거리가 먼 node와의 거리
res = max(result2)

print(res)
