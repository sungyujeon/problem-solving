# 백준 2635번 S5
# 수 이어가기
import sys

input = sys.stdin.readline

x = int(input())


def seq(a, b):
    li = [a, b]
    while li[-2]-li[-1] > -1:
        li.append(li[-2]-li[-1])
    
    return (len(li), li)


max_len = 0
result_list = []
for i in range(1, x+1):
    res = seq(x, i)
    
    if res[0] > max_len:
        max_len = res[0]
        result_list = res[1]

print(max_len)
print(' '.join(list(map(str, result_list))))




# start = x
# end = 0
# max_len = 0

# def seq(a, b):
#     li = [a, b]
#     while li[-1] > -1:
#         li.append(li[-2]-li[-1])
    
#     return (len(li)-1, li[:-1])

    

# def binary(start, end):
#     global max_len
#     global x
#     li = []
#     while start != end:
#         mid = (start + end) // 2
#         res = seq(x, mid)
#         if res[0] > max_len:
#             max_len = res[0]
#             li = res[1]
#             end = mid
#         else:
#             start = mid

#     return li

# result = list(map(str, binary(start, end)))
# print(max_len)
# print(' '.join(result))