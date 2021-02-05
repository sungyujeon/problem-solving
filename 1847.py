# 백준 1847번 S3
# 스택 수열
# import sys

# input = sys.stdin.readline

# n = int(input())
# seq = []
# for _ in range(n):
#     seq.append(int(input()))
n = 8

flag = [8,7,6,5,4,3,2,1]
seq = [4, 3, 6, 8, 7, 5, 2, 1]

start = list(seq)
tmp = []
end = []

result = []
while start:
    if start[-1] == n:
        end.append(start.pop())
        result.append('+')
    else:
        if not end:
            # end 비어있으면
            tmp.append(start.pop())
            result.append('-')
        else:
            # end 비어있지 않으면
            if start[-1] == end[-1] -1: 
                end.append(start.pop())
                result.append('+')
            elif tmp:
                if tmp[-1] == end[-1] -1:
                    end.append(tmp.pop())
                    result.append('-')
                else:
                    tmp.append(start.pop())
                    result.append('+')

while tmp:
    end.append(tmp.pop())

if end == flag:
    print(result)
else:
    print("NO")