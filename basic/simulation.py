# 구현(Implementation)
# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제
# 알고리즘은 간단한데 코드가 길어지는 문제, 실수 연산을 다루고 특정 소수점 자리까지 출력해야 하는 문제, 문자열 문제, 적절한 라이브러리 사용해야 하는 문제

#1 상하좌우 문제
# N x N 공간 위에 상하좌우로 이동하며 시작 좌표는 항상 (1,1) LRUD 계획서가 적혀있고, 막혀있으면 무시
# 최종적으로 도착할 좌표 출력
# 1 <= N <= 100

def solution1(N, plans):
    plans = plans.split()
    d = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, -1),
        'D': (0, 1)
    }

    i, j = 0, 0
    for plan in plans:
        di, dj = d[plan]
        ni = i + di
        nj = j + dj
        
        if (0 <= ni < N and 0 <= nj < N):
            i = ni
            j = nj
    return (j+1, i+1)

N = 5
plans = 'R R R U D D'
print(solution1(N, plans))


#2 시간 문제
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되어 있는 모든 경우의 수를 구하라
# 0 <= N <= 23
# 5 => 11475
def solution2(n):
    # 1초:1, 10초:14 1분:180, 10분:1260, 시간: if n < 3 1260 * n, 3 <= n < 12, 12 <= n < 23, n = 23
    cnt = 0
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    cnt += 1
    return cnt

N = 5
print(solution2(N))


#3 왕실의 나이트
# 나이트는 L자 형태로만 이동
# 나이트가 이동할 수 있는 경우의 수
def solution3(loc):
    j, i = list(loc)
    cdj = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    i, j = int(i) - 1, cdj.index(j)
    
    di = [2, 2, -2, -2, 1, 1, -1, -1]
    dj = [-1, 1, -1, 1, -2, 2, -2, 2]

    cnt = 0
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        
        if 0 <= ni < 8 and 0 <= nj < 8:
            cnt += 1
    return cnt

loc = 'a1'
print(solution3(loc))


#4 문자열 재정렬
# 알파멧 대문자와 숫자(0~9)로만 구성된 문자열. 이 때 모든 알파벳을 오름차순으로 정렬해 출력 후 그 뒤에 모든 숫자를 더한 값을 이어서 출력
def solution4(S):
    S = list(S)
    alpha = []
    num = []

    for s in S:
        if s.isalpha():
            alpha.append(s)
        else:
            num.append(s)
    alpha.sort()

    if num:
        num = str(sum(list(map(int, num))))
    else:
        num = ''

    return ''.join(alpha) + num
    
s = 'KKACB'
print(solution4(s))
