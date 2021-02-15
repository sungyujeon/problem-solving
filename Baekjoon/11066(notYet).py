# 백준 11066번 G3
# 파일 합치기

import sys

input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     pass
papers = [1, 21, 3, 4, 5, 35, 5, 4, 3, 5, 98, 21, 14, 17, 32]
papers = [40, 30, 30, 50]
total = 0
while len(papers) > 1:
    papers.sort()
    a = papers.pop(0)
    b = papers.pop(0)

    total += a + b
    papers.append(a+b)


# 첫번째 수가 
        