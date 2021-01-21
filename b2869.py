# 백준 2869번
# 달팽이
'''
<문제>
땅에 달팽이가 있습니다. 지상에서 측정 한 높이가 V 미터 인 나무 기둥의 꼭대기까지 올라 가려고합니다.
하루에 A 미터를 위로 올라갈 수 있지만, 매일 밤 잠을자는 동안 B 미터를 아래로 내려갑니다.
정상에 오르는 데 필요한 일수를 결정하십시오. 

<입력>
첫 번째이자 유일한 입력 줄에는 A, B 및 V (1 ≤ B <A ≤ V ≤ 1,000,000,000)라는
단일 공백으로 구분 된 세 개의 정수가 포함되며 위에서 설명한 의미가 있습니다. 

<출력>
첫 번째이자 유일한 출력 줄에는 달팽이가 맨 위에 도달하는 데 필요한 일 수가 포함되어야합니다. 
'''
from math import ceil

# A, B, V 입력
A, B, V = map(int, input().split(" "))

#1 높이에 대한 이항 연산 이용
def snail(day, night, height):
    return ceil((height - night) / (day - night))

#2 반복문 / 시간초과
def snail(day, night, height):
    days = 0
    climb_H = 0
    while True:
        # 날이 밝아서 올라가기 시작
        days += 1
        climb_H += day
        
        # 낮 동안 목표 도달하면 return
        if climb_H >= height:
            return days
        
        # 밤
        climb_H -= night

# 출력
print(snail(V, A, B))