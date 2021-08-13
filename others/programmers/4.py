# N으로 표현

# (number * N) / N
# (number / N) * N
# (number + N) - N
# (number - N) + N


def solution(N, number):
    answer = 0

    
    def bfs(n, num):
        num_set = set()
        
        num_set.add(n * num)
        num_set.add(n / num)
        num_set.add(n + num)
        num_set.add(n - num)
        num_set.add(num * n)
        num_set.add(num / n)
        num_set.add(num + n)
        num_set.add(num - n)

        
        

    return answer

N = 5
number = 12
solution(N, number)