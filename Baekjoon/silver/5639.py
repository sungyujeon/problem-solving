# 백준 5639번 S1
# 이진 검색 트리

# 전위 순회한 결과를 기준으로 이분 탐색 방식으로 진행
# 전위 순회한 숫자의 리스트 중에 root 보다 큰 값이 나오면 나눠서 다시 실행
# sys.stdin = open('input.txt')

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def f(start, end):
    if start > end:
        return
    else:
        root = pre[start]
        div = end +1

        for i in range(start+1, end+1):
            if root < pre[i]:
                div = i
                break
        f(start+1, div-1)
        f(div, end)
        print(root)
    
pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break
f(0, len(pre)-1)
