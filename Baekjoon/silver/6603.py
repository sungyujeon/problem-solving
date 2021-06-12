# 백준 6603번 S2
# 로또
# sys.stdin = open('input.txt', 'r')

import sys
from itertools import combinations
input = sys.stdin.readline

# 직접 구현
def comb(li, r):

    def generate(chosen):
        if len(chosen) == r:
            print(*chosen)
            return
        
        start = li.index(chosen[-1]) + 1 if chosen else 0
        for i in range(start, len(li)):
            chosen.append(li[i])
            generate(chosen)
            chosen.pop()
    generate([])

while True:
    li = list(map(int, input().split()))
    if len(li) == 1 and li[-1] == 0:
        break

    k = li[0]
    li = li[1:]
    li.sort()

    # 직접 구현
    # comb(li, 6)

    # itertools combination 사용
    comb_list = list(combinations(li, 6))
    for c in comb_list:
        print(*c)
    print()
    

    
    
    