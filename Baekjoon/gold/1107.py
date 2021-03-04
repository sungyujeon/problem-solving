# 백준 1107번 G5
# 리모컨
import sys

input = sys.stdin.readline

n = int(input())
list_n = list(str(n))
m = int(input())
a = [1 for _ in range(10)]

if m != 0:
    broken = list(map(int, input().split()))
    for i in broken:
        a[i] = 0

cnt = abs(n - 100)
for i in range(1000001):
    list_i = list(str(i))
    flag = 0
    for c in list_i:
        if a[int(c)] == 1:
            continue
        else:
            flag = 1
            break

    if flag:
        continue
    else:
        cnt = min(cnt, abs(n - i) + len(list_i))

print(cnt)



# def find_up(num, _broken):
#     while num < 1000001:
#         flag = False
#         for i in _broken:
#             if str(num).find(i) != -1:  # 고장난게 있으면
#                 flag = True
#                 break
        
#         if flag:  # 고장난게 있으면
#             num += 1
#         else:
#             return num
    
#     return 1000001

# def find_down(num, _broken):
#     while num > 0:
#         flag = False
#         for i in _broken:
#             if str(num).find(i) != -1:  # 고장난게 있으면
#                 flag = True
#                 break
        
#         if flag:  # 고장난게 있으면
#             num -= 1
#         else:
#             return num
    
#     return 1000001


# n = int(input())
# m = int(input())
# broken = input().strip().split()

# res1 = abs(n-100)
# res2 = find_up(n, broken)
# res3 = find_down(n, broken)

# res2 = len(str(res2)) + abs(n-res2)
# res3 = len(str(res3)) + abs(n-res3)

# result = min(res1, res2, res3)

# print(result)
