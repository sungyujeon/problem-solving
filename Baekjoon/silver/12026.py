# 백준 12026번 S1
# BOJ 거리

import sys
input = sys.stdin.readline

def dfs(_way, _n):
    stack = [('B', 0)]
    depth= 0

    while stack:
        char, idx = stack.pop()
        
        if idx == _n:  # 끝까지 옴
            pass
        else:
            if char == 'B':
                for i in range(i+1, _n):
                    if _way[i] == 'O':  # 갈 수 있으면
                        stack.append(('O', i))
                    else:
                        if i == _n:
                            break
                else:  # 중간에 갈 곳이 있음
                    pass

            elif char == 'O':
                pass
            else:  # 'J'
                pass
    



n = int(input())
way = list(input().rstrip())
