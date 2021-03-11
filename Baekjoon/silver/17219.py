# 백준 17219번 S4
# 비밀번호 찾기

import sys

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n, m = map(int, input().split())

pwd_dict = {}
for _ in range(n):
    site, pwd = input().split()
    pwd_dict[site] = pwd

for _ in range(m):
    a = input().rstrip()
    print(pwd_dict.get(a))


    