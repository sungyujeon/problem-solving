# 백준 2609번 S5
# 최대공약수와 최소공배수

# GCF : Greatest Common Factor
# LCM : Least Common multiple
import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

def gcf(a, b):
    while b != 0:
        a = a % b
        a, b = b, a
    return a

G = gcf(a, b)
L = int(a * b / G)
print(G)
print(L)