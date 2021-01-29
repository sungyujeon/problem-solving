# 백준 8958번
# Score

n = int(input())

scores = []
for _ in range(n):
    scores.append(input())

def cal_score(score_str):
    total = 0
    tmp_score = 0
    for i in score_str:
        if i == 'O':
            tmp_score += 1
            total += tmp_score
        else:
            tmp_score = 0
    return total

for score in scores:
    print(cal_score(score))