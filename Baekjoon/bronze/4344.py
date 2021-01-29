# 백준 4344번
# 평균은 넘겠지

n = int(input())

students_score = []
for _ in range(n):
    students_score.append(list(map(int, input().split())))

for scores in students_score:
    num = scores.pop(0)
    avg = sum(scores) / num

    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1
        div = cnt / num * 100
    print('{0:.3f}%'.format(div))