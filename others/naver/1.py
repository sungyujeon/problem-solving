
def solution(lottery):
    tries = [0] * 1001
    winners = set()

    for user, isWin in lottery:
        if user not in winners:
            tries[user] += 1

            if isWin:
                winners.add(user)

    if not winners:
        return 0
    else:
        total = 0
        for winner in winners:
            total += tries[winner]
        
        res = total // len(winners)
        return res

lottery = [[1,0],[2,0],[3,0]]
print(solution(lottery))