# 프로그래머스 위클리챌린지 12주차
# 피로도

def dfs(k, curr, total, used, dungeons, n):
    if curr > total:
        total = curr

    for i in range(n):
        minimum, spend = dungeons[i]
        
        if not used[i] and k >= minimum:
            used[i] = True
            total = dfs(k-spend, curr+1, total, used, dungeons, n)
            used[i] = False
    
    return total

def solution(k, dungeons):
    n = len(dungeons)
    used = [False] * n
    
    return dfs(k, 0, 0, used, dungeons, n)

k = 80
dungeons = [[80,20],[50,40],[30,30]]
print(solution(k, dungeons))