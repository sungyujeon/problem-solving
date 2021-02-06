# 백준 1874번 S3
# 스택 수열
import sys

input = sys.stdin.readline

n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))

flag = [i for i in range(n, 0, -1)]

start = list(seq)
tmp = []
end = []

result = []

tmp.append(start.pop())
result.append('-')
while start:
    if end:
        if tmp:
            if tmp[-1] == end[-1] - 1:
                end.append(tmp.pop())
                result.append('+')
            else:
                tmp.append(start.pop())
                result.append('-')
        else:
            tmp.append(start.pop())
            result.append('-')
    else:
        if tmp[-1] == n:
            end.append(tmp.pop())
            result.append('+')
        else:
            tmp.append(start.pop())
            result.append('-')

while tmp:
    end.append(tmp.pop())
    result.append('+')
    
# while start:
#     if start[-1] == n:
#         end.append(start.pop())
#         result.append('+')
#     else:
#         if not end:
#             # end 비어있으면
#             tmp.append(start.pop())
#             result.append('+')
#         else:
#             # end 비어있지 않으면
#             if start[-1] == end[-1] -1: 
#                 end.append(start.pop())
#                 result.append('+')
#             elif tmp:
#                 if tmp[-1] == end[-1] -1:
#                     end.append(tmp.pop())
#                     result.append('-')
#                 else:
#                     tmp.append(start.pop())
#                     result.append('+')

# while tmp:
#     end.append(tmp.pop())
#     result.append('-')
if end == flag:
    result.reverse()
    for i in result:
        print(i)
else:
    print("NO")