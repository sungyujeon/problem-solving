import sys
sys.stdin = open('input3.txt', 'r')

def find_set(num):
    global pa

    while pa[num] != num:
        num = pa[num]    
    return num


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    tmp_li = list(map(int, input().split()))
    
    # 자기 자신으로 편성
    pa = [-1] * (n+1)
    for i in range(1, n+1):
        pa[i] = i

    # 배정
    for i in range(m):
        p, c = tmp_li[2*i], tmp_li[2*i+1]
        if p > c:
            p, c = c, p
        pa[c] = find_set(p)
    print(pa)
    # 조 찾기
    res = 0
    for i in range(1, n+1):
        if pa[i] == i:
            res += 1

    print(f'#{tc} {res}')