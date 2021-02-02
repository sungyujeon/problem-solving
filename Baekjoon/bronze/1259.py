# 백준 1259번 B1
# 팰린드롬수
import sys

def isPalindrome(n):
    if not len(n):
        return 'yes'
    if n[0] == n[len(n) - 1]:
        n = n[1:-1]
        return isPalindrome(n)
    else:
        return 'no'

t = ''
while True:
    t = sys.stdin.readline().strip()
    if t == '0':
        break
    print(isPalindrome(t))