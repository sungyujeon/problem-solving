# 백준 18870번 S2
# 좌표 압축
import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

li_dict = {}
li_sorted = sorted(list(set(li)))

for k, v in enumerate(li_sorted):
    li_dict[v] = k

result = ''
for i in li:
    result += str(li_dict[i]) + ' '

print(result[:-1])



# n = int(input())
# li = list(map(int, input().split()))

# li_dict = {}
# li_sorted = sorted(li)
# li_sorted.insert(0, li_sorted[0]-1)

# flag = 0
# for i in range(1, len(li_sorted)):
#     value = li_sorted[i]
#     if value != li_sorted[i-1]:  # i-1 idx와 값이 같으면(같은 값)
#         li_dict[value] = flag
#         flag += 1

# result = ''
# for i in li:
#     result += str(li_dict[i]) + ' '

# print(result[:-1])

