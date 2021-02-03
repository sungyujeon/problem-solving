# 백준 2798번 B2
# 블랙잭
import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().strip().split()))

idx = len(cards)
max = 0
for i in range(idx-2):
    for j in range(i+1, idx-1):
        for k in range(j+1, idx):
            tmp_max = cards[i] + cards[j] + cards[k]
            if max < tmp_max <= m:
                max = tmp_max
print(max)



# check = [False] * 3
# card_tracking = []
# def blackjack():
#     pass