# H-index

def solution(citations):
    answer = 0

    citations.sort()
    n = len(citations)
    # [0,1,3,5,6]
    for i in range(n):
        h = citations[i]
        cnt = n - i
        if cnt <= h:
            answer = cnt
            break
    
    return answer

citations = [3,0,6,1,5]
print(solution(citations))