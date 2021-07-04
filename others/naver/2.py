def solution(grid):
    answer = 0
    r, c = len(grid), len(grid[0])

    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0:
                grid[i][j] += grid[i-1][j]
            else:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    answer = grid[r-1][c-1]
    return answer

grid = [ [1, 2], [3, 4] ]
print(solution(grid))