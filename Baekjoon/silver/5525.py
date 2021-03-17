# 백준 5525번 S2
# IOIOI

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

# check_n = 'I' + ('OI' * n)

ans = 0
cnt = 0
i = 1

while i < m -1:
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        cnt += 1
        if cnt == n:
            cnt -= 1
            ans += 1
        i += 1
    else:
        cnt = 0
    i += 1

print(ans)