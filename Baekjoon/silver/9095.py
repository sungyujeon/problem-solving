# 백준 9095번 S3
# 1,2,3 더하기
import sys

input = sys.stdin.readline
T = int(input())

s = [0, 1, 2, 4] + [0] * 7
for i in range(4, 11):
    s[i] = s[i-3] + s[i-2] + s[i-1]
for _ in range(T):
    n = int(input())
    print(s[n])