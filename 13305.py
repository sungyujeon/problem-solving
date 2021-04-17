# 백준 13305번 S4
# 주유소

# sys.stdin = open('input3.txt', 'r')
import sys
input = sys.stdin.readline

n = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))

total = 0
fuel_cost = costs[0]
for i in range(n-1):
    total += fuel_cost * dists[i]
    if costs[i+1] < fuel_cost:
        fuel_cost = costs[i+1]
print(total)