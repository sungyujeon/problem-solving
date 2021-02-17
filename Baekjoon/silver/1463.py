# 백준 1463번 S3
# 1로 만들기

testcase=int(input())
 
dp=[ 0 for _ in range(testcase+2) ]
dp[2]=1
 
for i in range(2, len(dp)):
 
    dp[i]=dp[i-1]+1
 
    if i%3==0:
        if dp[i]> dp[int(i/3)]+1:
            dp[i]=dp[int(i/3)]+1
    if i%2==0:
        if dp[i]> dp[int(i/2)]+1:
            dp[i] =dp[int(i/2)]+1
 
print(dp[testcase])


# import sys

# input = sys.stdin.readline

# n = int(input())

# li = [0 for _ in range(n+1)]

# li[0] = li[1] = 0
# li[2] = li[3] = 1


# for i in range(4, len(li)):
#     li[i] = li[i-1]+1

#     if i % 3 == 0:
#         if li[i] > li[i//3]+1:
#             li[i] = li[i//3]+1
#     elif i % 2 == 0:
#         if li[i] > li[i//2]+1:
#             li[i] = li[i//2]+1

# print(li[n])


# def check(n):
#     if n in [0, 1]:
#         return 0

#     if not li[n]:
#         if n % 2 != 0 and n % 3 !=0:
#             li[n] = check(n-1) + 1
#         else:
#             if not n % 3:
#                 li[n] = check(n//3) + 1
#             elif not n % 2:
#                 li[n] = min(check(n-1)+1, check(n//2)+1)
#             else:
#                 li[n] = check(n-1)+1
#     return li[n]
# print(check(n))


