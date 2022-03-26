def solution(abilities, k):
    answer = 0

    N = len(abilities)
    abilities.sort(reverse=True)
    if N % 2:
        abilities.append(0)

    ks = []
    for i in range(0, N, 2):
        s1, s2 = abilities[i], abilities[i+1]
        ks.append((abs(s1-s2), i))
    
    ks.sort(reverse=True)
    ks = ks[:k]
    ks = set((map(lambda x: x[1], ks)))

    for i in range(0, N, 2):
        s1, s2 = abilities[i], abilities[i+1]
        if i in ks:
            answer += max(s1, s2)
        else:
            answer += min(s1, s2)
    
    return answer

abilities = [9, 9, 8, 6, 3, 2, 1, 1]
abilities = [10, 9, 8, 7, 6]
k = 1
print(solution(abilities, k))