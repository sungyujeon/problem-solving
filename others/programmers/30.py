# programmers 네트워크

def solution(n, computers):
    def dfs(_n, _computers, _used, ci):
        stack = [ci]
        
        while stack:
            node = stack.pop()
            for k in range(_n):
                if (node != k and not used[k] and (_computers[node][k] or _computers[k][node])):
                    used[k] = True
                    stack.append(k)
                
    
    answer = 0
    used = [False for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if (i != j and computers[i][j] and not used[i]):
                used[i] = True
                dfs(n, computers, used, i)
                answer += 1
                
    for k in range(n):
        if not used[k]:
            answer += 1
            

    return answer