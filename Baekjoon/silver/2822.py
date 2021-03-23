# 백준 2822번 S5
# 점수 계산
import sys

input = sys.stdin.readline

scores = []
for i in range(8):
    score = int(input())
    scores.append((score, i+1))

scores.sort(reverse=True)

total = 0
res = []
for i in range(5):
    total += scores[i][0]
    res.append(scores[i][1])

res.sort()
res = list(map(str, res))

print(total)
print(' '.join(res))



