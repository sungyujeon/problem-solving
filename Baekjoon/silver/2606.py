# 백준 2606번 S3
# 바이러스
import sys

input = sys.stdin.readline

com_cnt = int(input())
pair_cnt = int(input())

# com_dict 초기화
com_dict = {}
for i in range(1, com_cnt+1):
    com_dict[i] = []


# 컴퓨터 연결하면 해당 key의 value배열에 연결된 컴퓨터 추가
for _ in range(pair_cnt):
    a, b = map(int, input().split())
    
    com_dict[a].append(b)
    com_dict[b].append(a)
    

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)

visited = []
dfs(1, com_dict)
print(len(visited)-1)

# 상호 연결된 것들이 앞에서 정의되고, 1번 컴퓨터와 연결된 컴퓨터가 뒤에서 정의되면 앞에 것은 무시되어서 1번 컴퓨터 배열에 추가되지 않음
# # com_dict 초기화
# com_dict = {}
# for i in range(1, com_cnt+1):
#     com_dict[i] = []

# # 컴퓨터 연결하면 해당 key의 value배열에 연결된 컴퓨터 추가
# for _ in range(pair_cnt):
#     a, b = map(int, input().split())
    
#     com_dict[a].append(b)
#     com_dict[b].append(a)

# # 모든 컴퓨터를 돌면서
# for k, v in com_dict.items():
#     if k in com_dict[1]:  # key가 1번 컴퓨터와 연결되어 있으면 key와 연결된 컴퓨터(value)도 1번 컴퓨터 배열에 추가
#         com_dict[1].extend(v)
#     else:  # 해당 key가 1번 컴퓨터 배열에 없어도 key와 연결된 value 컴퓨터 중에 1번 컴퓨터와 연결된 것이 있으면 해당 key 컴퓨터와 value 컴퓨터들 모두 1번 컴퓨터 배열에 추가
#         for i in v:
#             if i in com_dict[1]:
#                 com_dict[1].extend(v)
#                 com_dict[1].append(k)
#                 break

# # 1번 컴퓨터에 추가된 컴퓨터들 중복 제거
# # 1번 컴퓨터 1개를 제외한 result 출력(result-1)
# result = len(set(com_dict[1]))
# print(result-1)



# 왠 안되는거지???
# for k, v in com_dict.items():
#     try:
#         v.index(1)
#         com_dict[1].extend(v)
#     except:
#         pass

# result = len(set(com_dict[1]))

# print(result-1)

# 13 41 

# 아래 방법은 이미 연결되어 있던 컴퓨터 리스트들이 나중에 1과 연결되었을 때 연결이 안됨
# com_list = [1]
# for _ in range(pair_cnt):
#     a, b = map(int, input().split())

#     if a in com_list or b in com_list:
#         com_list.extend([a, b])

# com_set = set(com_list)
# print(len(com_set)-1)
        
