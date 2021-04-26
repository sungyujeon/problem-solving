# 백준 10610번 S5
# 30

import sys
input = sys.stdin.readline

n = input().rstrip()
n_int = list(map(int, n))

try:
    zero_idx = n.index('0')
    if sum(n_int) % 3 == 0:
        n_int.sort(reverse=True)
        n_int = list(map(str, n_int))
        print(''.join(n_int))
    else:
        print(-1)
except:
    print(-1)
