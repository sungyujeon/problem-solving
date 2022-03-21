# Programmers
# 주식가격 stack

def solution(prices):
    n = len(prices)
    ans = [0] * n
    
    for i in range(n-1):
        price = prices[i]
        for j in range(i+1, n):
            ans[i] += 1
            if price > prices[j]:
                break

    return ans

# 효율성
def solution(prices):
    n = len(prices)
    stack = []
    answer = [0] * n
    for i in range(n):
        if not stack:
            while not stack and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])

    for i, _ in stack:
        answer[i] = n - 1 - i

    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))


