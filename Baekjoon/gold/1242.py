# 백준 1242번 G2
# 소풍
import sys
input = sys.stdin.readline

# def picnic2(N, K, M):
#     count = 1
#     while True:
#         if K > N:
#             k = K % N
#             if k == 0:
#                 k = N
#         else:
#             k = K
#         if k == M:
#             break
#         if M - k > 0:
#             M = M - k
#         elif M - k < 0:
#             M = M - k + N
#         N -= 1
#         count += 1
#     return count

# N, K, M = map(int, input().split())
# print(picnic2(N, K, M))


n, k, m = map(int, input().split())


# 정답 코드
# m -= 1

# start = 0
# cnt = 1
# while True:
#     removed = (start + k - 1) % n

#     if removed == m:
#         break
#     elif removed < m:
#         m -= 1
    
#     start = removed
#     n -= 1
#     cnt += 1

# print(cnt)

cnt = 1
while True:
    target = k
    if target > n:
        target %= n
        if target == 0:
            target = n

    if target == m:
        break
    
    m -= target
    if m < 0:
        m += n
    cnt += 1
    n -= 1
print(cnt)





# 틀린 풀이
# def fail(_n, _k, _m):
#     depth = 0
#     pop_num = 0
#     del_num = 0
    
#     while True:
#         pop_num += k + depth
#         depth += 1

#         if pop_num > n:
#             pop_num %= n
        
#         if pop_num == _m:
#             return depth