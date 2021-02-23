# 백준 2116번 G5
# 주사위 쌓기
import sys
import copy

input = sys.stdin.readline

n = int(input())

dices = []
for _ in range(n):
    dice = list(map(int, input().split()))
    dices.append(dice)

flag_dict = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0,
}

# 첫번째 주사위를 1~6 선택할 때마다
result = 0
for i in range(1, 7):
    # total
    total = 0

    down_num = i
    dices2 = copy.deepcopy(dices)
    for dice in dices2:
        down_idx = dice.index(down_num)
        up_idx = flag_dict[down_idx]
        up_num = dice[up_idx]

        dice.remove(down_num)
        dice.remove(up_num)

        # 각 주사위의 가장 큰 값
        total += max(dice)

        down_num = up_num
    
    if total > result:
        result = total

print(result)