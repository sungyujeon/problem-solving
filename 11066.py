# 백준 11066번 G3
# 파일 합치기
import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()

    