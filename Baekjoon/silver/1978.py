# 백준 1978번 S4
# 소수 찾기
import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1/2)) + 1):
        if not n % i:
            return False
    return True

prime_numbers = []
for num in nums:
    if isPrime(num):
        prime_numbers.append(num)

print(len(prime_numbers))

