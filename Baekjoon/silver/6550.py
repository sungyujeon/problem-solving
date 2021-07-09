# 백준 6550번 S5
# 부분 문자열
# sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

def solution(s, t):
    i = 0
    for char in s:
        for j in range(i, len(t)):
            if t[j] == char:
                i = j+1
                break
            elif j == len(t)-1:
                return False
    return True

while True:
    try:
        S, T = input().split()
        res = solution(S, T)            
        res = 'Yes' if res else 'No'
        print(res)
    except:
        break