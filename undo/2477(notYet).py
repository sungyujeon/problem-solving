# 백준 2477번 S5
# 참외밭

import sys

input = sys.stdin.readline

n = int(input())

direction_dict = {
    1: (1,0),
    2: (-1,0),
    3: (0,-1),
    4: (0,1),

}


x_list = []
y_list = []
x = 0
y = 0
for _ in range(n):
    direction, length = map(int, input().split())
    
    dir_flag = direction_dict.get(direction)
    x += dir_flag[0] * length
    y += dir_flag[1] * length

    x_list.append(x)
    y_list.append(y)

x_list.sort()
y_list.sort()

# area
x_max = x[-1]
x_min = x[0]
y_max = y[-1]
y_min = y[0]

area = (x_max - x_min) * (y_max - y_min)

# remained area

    