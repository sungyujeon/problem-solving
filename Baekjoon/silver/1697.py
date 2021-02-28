# 백준 1697번 S1
# 숨바꼭질

import sys
from collections import deque

input = sys.stdin.readline

def whereNum(n, k):
    visited = [0] * 100001
    queue = deque()
    depth = 1

    queue.append(k)
    queue.append(True)
    visited[k] = 1
    while queue:
        num = queue.popleft()

        if num is True:  # flag가 True이면 모든 breadth를 돌았으므로 depth += 1
            depth += 1
            queue.append(True)
        else:
            if num % 2:  # 홀수이면
                tmp1 = num - 1
                tmp2 = num + 1
                
                if tmp1 == n or tmp2 == n:  # 찾으려는 n이 있으면 break
                    return depth
                else:
                    if 0 <= tmp1 < 100001 and visited[tmp1] == 0:
                        queue.append(tmp1)
                        visited[tmp1] = 1
                    
                    if 0 <= tmp2 < 100001 and visited[tmp2] == 0:
                        queue.append(tmp2)
                        visited[tmp2] = 1

            else:  # 짝수이면
                tmp1 = num // 2
                tmp2 = num - 1
                tmp3 = num + 1

                if tmp1 == n or tmp2 == n or tmp3 == n:
                    return depth
                else:
                    if 0 <= tmp1 < 100001 and visited[tmp1] == 0:
                        queue.append(tmp1)
                        visited[tmp1] = 1
                    
                    if 0 <= tmp2 < 100001 and visited[tmp2] == 0:
                        queue.append(tmp2)
                        visited[tmp2] = 1

                    if 0 <= tmp3 < 100001 and visited[tmp3] == 0:
                        queue.append(tmp3)
                        visited[tmp3] = 1



n, k = map(int, input().split())
if n == k:
    result = 0
else:
    result = whereNum(n, k)

print(result)