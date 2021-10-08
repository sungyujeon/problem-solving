# 프로그래머스 위클리 챌린지 6주차 
# 복서 정렬하기

def solution(weights, head2head):
    n = len(weights)
    answer = [0 for _ in range(n)]
    
    infos = [{ 'id': i+1, 'upperWins': 0, 'rate': 0.0, 'weight': weights[i] } for i in range(n)]
    
    for i in range(n):
        _win = 0
        _upperWin = 0
        _lose = 0
        for j in range(n):
            if (i == j):
                continue
            
            if head2head[i][j] == 'W':
                _win += 1
                if weights[i] < weights[j]:
                    _upperWin += 1
            elif head2head[i][j] == 'L':
                _lose += 1 
    
        rate = 0
        totalPlay = _win + _lose
        if totalPlay != 0:
            rate = _win / (_win + _lose)
        infos[i]['rate'] = rate
        infos[i]['upperWins'] = _upperWin
        
    infos.sort(key=lambda x: (x['rate'], x['upperWins'], x['weight']), reverse=True)
    
    for i in range(n):
        answer[i] = infos[i]['id']

    return answer
    

weights = [50,82,75,120]
head2head = ["NLWL","WNLL","LWNW","WWLN"]
print(solution(weights, head2head))