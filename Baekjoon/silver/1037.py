# 백준 1037번 S5
# 약수

import sys
input = sys.stdin.readline

n = int(input())
divisors = list(map(int, input().split()))

divisors.sort()
print(divisors[0] * divisors[-1])