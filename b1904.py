# 백준 1904번
# 01타일

mem = [0] * 1000001
mem[1] = 1
mem[2] = 2

n = int(input())
for i in range(3, n+1):
    mem[i] = (mem[i-2] + mem[i-1]) % 15746
print(mem[n])