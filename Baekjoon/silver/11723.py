# 백준 11723번 S5
# 집합

import sys

input = sys.stdin.readline

s = set()
n = int(input())

for i in range(n):
    tmp = input().strip().split()

    if len(tmp) == 1:
        if tmp[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue
    
    query, target = tmp[0], tmp[1]
    target = int(target)

    if query == 'add':
        s.add(target)
    elif query == 'check':
        print(1 if target in s else 0)
    elif query == 'remove':
        s.discard(target)
    elif query == 'toggle':
        if target in s:
            s.discard(target)
        else:
            s.add(target)




# s = []
# def toggle(x):
#     if x not in s:
#         s.append(x)
#     else:
#         s.remove(x)

# m = int(input())

# for _ in range(m):
#     query = input().strip().split()

#     if len(query) == 1:
#         if query[0] == 'all':
#             s = [str(i) for i in range(1, 21)]
#         else:
#             s = []
#         continue

#     query1 = query[0]
#     query2 = query[1]
#     if query1 == 'add':
#         s.append(query2)
#     elif query1 == 'remove':
#         s.remove(query2)
#     elif query1 == 'check':
#         result = 1 if query2 in s else 0
#         print(result)
#     elif query1 == 'toggle':
#         toggle(query2)
#     else:
#         continue
    
