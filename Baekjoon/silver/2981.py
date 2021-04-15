# 백준 2981번 S1
# 검문
# 나머지가 같은 수들의 성질
# A = G*a + R
# B = G*b + R
# A-B = G(a-b)
# 따라서 A, B는 G의 약수로 나누었을 때 나머지가 같다

from math import gcd
import sys
input = sys.stdin.readline

n = int(input())
li = [0] * n
for i in range(n):
    li[i] = int(input())

# 내림차순으로 정렬
li.sort(reverse=True)

# 각 숫자의 차를 저장하는 list
li_diff = [0] * (n-1)
for i in range(n-1):
    li_diff[i] = li[i] - li[i+1]

# li_diff의 최대공약수
res_gcd = li_diff[0]
for i in range(n-1):
    res_gcd = gcd(res_gcd, li_diff[i])

# 위 최대공약수의 약수
res_list = []
for i in range(1, int((res_gcd ** (1/2)) + 1)):
    if res_gcd % i == 0:
        res_list.append(i)
        if i ** 2 != res_gcd:
            res_list.append(res_gcd // i)
res_list.sort()
print(*res_list[1:])
