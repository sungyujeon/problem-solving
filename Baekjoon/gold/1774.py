# 백준 1774번 G4
# 우주신과의 교감
# sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

def comb(_n, _tmp_li, _li):
    idx = 0
    for i in range(_n-1):
        for j in range(i+1, _n):
            x1, y1 = _tmp_li[i]
            x2, y2 = _tmp_li[j]
            
            dist = (((x1-x2) ** 2) + ((y1-y2) ** 2)) ** (1/2)
            _li[idx] = (i, j, dist)
            idx += 1


def find_set(num, _pa):
    while num != _pa[num]:
        num = _pa[num]
    return num


def Kruskal(_li):
    global n, m, pa

    total = 0
    cnt = m

    for k in _li:
        u, v, w = k
        
        pa_u = find_set(u, pa)
        pa_v = find_set(v, pa)

        if pa_u != pa_v:
            pa[pa_v] = pa[pa_u]
            total += w
            cnt += 1

    return total


n, m = map(int, input().split())
INF = 1500000
pa = [i for i in range(n)]
tmp_li = [[] * n for _ in range(n)]
for i in range(n):
    x, y = map(float, input().split())
    tmp_li[i] = (x, y)

for i in range(m):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    
    pa_u = find_set(u, pa)
    pa_v = find_set(v, pa)
    pa[pa_v] = pa[pa_u]

# 두 개의 정점과 정점 사이를 연결하는 거리를 저장하는 배열 생성
edges_n = (n * (n-1)) // 2
li = [[] * edges_n for _ in range(edges_n)]
comb(n, tmp_li, li)
li.sort(key=lambda x: x[2])

# MST
res = Kruskal(li)
print('{:.2f}'.format(res))