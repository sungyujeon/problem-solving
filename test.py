import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for i in range(n):
    if i == 0:
        coins.append(int(input()))
    else:
        coins.insert(0, int(input()))

cnt = 0
for coin in coins:
    if k // coin != 0:
        cnt += k // coin
        k = k % coin
    
    if not k:
        break
print(cnt)
