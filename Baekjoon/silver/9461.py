# 백준 9461 S3
# 파도반 수열

# if n >= 7
# P(N+1) = P(N) + P(N-4)
    
pado = [0] * 101
pado[1] = 1
pado[2] = 1
pado[3] = 1
pado[4] = 2
pado[5] = 2
pado[6] = 3
pado[7] = 4
for i in range(7, 100):
    pado[i+1] = pado[i] + pado[i-4]

N = int(input())
for _ in range(N):
    n = int(input())
    print(pado[n])