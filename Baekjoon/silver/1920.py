# 백준 1920번 S4
# 수 찾기
import sys
n = int(sys.stdin.readline())
n_list = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    result = 1 if i in n_list else 0
    print(result)