# 백준 11866번 S4
# 요세푸스 문제0

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

circle = list(range(1, n+1))

result = []
while circle:
    for _ in range(k-1):
        circle.append(circle.pop(0))
    result.append(circle.pop(0))

result = list(map(str, result))
result_format = ', '.join(result)
print(f'<{result_format}>')