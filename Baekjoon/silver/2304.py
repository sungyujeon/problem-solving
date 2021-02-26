# 백준 2304번 S2
# 창고 다각형
import sys

input = sys.stdin.readline

n = int(input())

# lh_list = [(2,4), (11,4), (15,8), (4,6), (5,3), (8, 10), (13,6)]
lh_list = []
for _ in range(n):
    a, b = map(int, input().split())
    lh_list.append((a, b))
lh_list.sort()

# idxs, heights
idxs = []
heights = []
for i in lh_list:
    idxs.append(i[0])
    heights.append(i[1])

max_h = max(heights)
max_h_idx = heights.index(max_h)


def calc_left():
    global idxs
    global heights
    global max_h_idx
    
    start_h_idx = max_h_idx
    left_h_li = heights[:start_h_idx]
    total = 0
    while left_h_li:
        left_h_li = heights[:start_h_idx]

        if left_h_li:
            left_max_h = max(left_h_li)
            left_max_h_idx = left_h_li.index(left_max_h)
            
            total += left_max_h * (idxs[start_h_idx] - idxs[left_max_h_idx])

        # left_max_h_idx를 start_h_idx로 할당
        start_h_idx = left_max_h_idx
    
    return total
    

def calc_right():
    global idxs
    global heights
    global max_h_idx
    
    start_h_idx = max_h_idx
    right_h_li = heights[start_h_idx+1:]
    total = 0
    while right_h_li:
        right_h_li = heights[start_h_idx+1:]

        if right_h_li:
            right_max_h = max(right_h_li)
            right_max_h_idx = right_h_li.index(right_max_h) + start_h_idx + 1
            
            right_idxs = idxs[right_max_h_idx]
            start_idxs = idxs[start_h_idx] + 1

            total += right_max_h * (right_idxs - start_idxs + 1)

        # left_max_h_idx를 start_h_idx로 할당
        start_h_idx = right_max_h_idx

    return total

# max를 기준으로 왼쪽 오른쪽
result = max_h
if max_h_idx == 0:  # 맨 왼쪽 값이 max_h
    result += calc_right()
elif max_h_idx == len(heights): # 맨 오른쪽 값이 max_h
    result += calc_left()
else:  # max_h가 가운데에 있으면
    result += calc_left() + calc_right()

print(result)
    


# for _ in range(n):
#     a, b = map(int, input().split())
#     lh_list.append((a, b))

# max 값을 기준으로 왼쪽과 오른쪽을 계산





# 포기
# lh_list.sort()

# heights = []
# for i in lh_list:
#     heights.append(i[1])

# result = 0
# start = 0
# end = 0
# i = 0
# while i < len(lh_list):
#     tmp_max_h = max(heights[i+1:])
    
#     height = lh_list[i][1]
#     start = lh_list[i][0]
    
#     if height < tmp_max_h:  # 다음 창고가 높으면
#         next_mh_idx = i+1 + heights[i+1:].index(tmp_max_h)
#         next_mh_loc = lh_list[next_mh_idx][0]
        
#         # 다음 높이까지의 넓이
#         tmp_area = height * abs(start - lh_list[next_mh_idx][0])
#         result += tmp_area

#         if next_mh_idx == len(lh_list)-1:
#             result += tmp_max_h

#         i += next_mh_idx
    
#     else:  # 다음 창고가 낮으면
#         height = height - tmp_max_h
#         result += height

#         next_mh_idx = i+1 + heights[i+1:].index(tmp_max_h)
#         next_mh_loc = lh_list[next_mh_idx][0]
        
#         result += tmp_max_h * abs(start - next_mh_loc)

#         if next_mh_idx == len(lh_list)-1:  # 마지막이면
#             result += tmp_max_h

#         i += next_mh_idx

# print(result)