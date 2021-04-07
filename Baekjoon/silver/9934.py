# 백준 9934번 S2
# 완전 이진 트리
import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


k = int(input())
li = list(map(int, input().split()))

res = [[] for _ in range(k)]

def binarysearch(_li, depth):
    global res

    if depth == k:
        return

    l = len(_li)
    root_idx = l // 2
    root = str(_li[root_idx])
    res[depth].append(root)

    left = _li[:root_idx]
    right = _li[root_idx+1:]

    binarysearch(left, depth+1)
    binarysearch(right, depth+1)

binarysearch(li, 0)

for i in res:
    print(' '.join(i))