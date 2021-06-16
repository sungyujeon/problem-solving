# 백준 1946번 S1
# 신입사원

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cnt = 1
    li = []
    
    N = int(input())
    for i in range(N):
        score1, score2 = map(int, input().split())
        li.append([score1, score2])

    li.sort()
    my_max = li[0][1]
    
    for i in range(1, N):
        if my_max > li[i][1]:
            cnt += 1
            my_max = li[i][1]

    print(cnt)