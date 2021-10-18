// 백준 16234번 G5
// 인구 이동

const fs = require('fs')
const stdin = fs.readFileSync('input.txt').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const isInBound = (i, j, N) => {
  if (0 <= i && i < N && 0 <= j && j < N) {
    return true
  }
  return false
}

const diff = (L, R, curr, next) => {
  const _diff = Math.abs(curr - next)

  if (L <= _diff && _diff <= R) {
    return true
  }
  return false
}

const getTotal = (qs, array) => {
  let total = 0
  for ([_i, _j] of qs) {
    total += array[_i][_j]
  }
  return total
}

const setAvg = (qs, avg, array) => {
  const newArray = [...array]
  for ([_i, _j] of qs) {
    newArray[_i][_j] = avg
  }
  array = newArray
}

const union = (array, N, L, R) => {
  const visited = Array.from(Array(N), () => new Array(N).fill(false))
  
  const dfs = (i, j, visited, N) => {
    const qs = new Set()
    const q = [[i, j]]

    while (q.length !== 0) {
      const [ci, cj] = q.pop()
      
      if (!visited[ci][cj]) {
        visited[ci][cj] = true
        const curr = array[ci][cj]

        for (const d of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
          const ni = ci + d[0]
          const nj = cj + d[1]
          
          if (isInBound(ni, nj, N) && !visited[ni][nj]) {
            const next = array[ni][nj]
            if (diff(L, R, curr, next)) {
              qs.add([ni, nj])
              q.push([ni, nj])
            }
          }
        }
      }
    }
    
    if (qs.size !== 0) {
      qs.add([i, j])
      const avg = (getTotal(qs, array) / qs.size) | 0
      setAvg(qs, avg, array)
      return 1
    }
    return 0
  }

  let flag_cnt = 0
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!visited[i][j]) {
        flag_cnt += dfs(i, j, visited, N)
      }
    }
  }

  if (flag_cnt === 0) {
    return false
  }
  return true
}

const solution = (array, N, L, R) => {
  let flag = true
  let cnt = -1
  while (flag) {
    flag = union(array, N, L, R)
    cnt++
  }
  return cnt
}

const [N, L, R] = input().split(' ').map(Number)
const array = Array.from(Array(N), () => input().split(' ').map(Number))
console.log(solution(array, N, L, R))
// 0~n
// dfs로 돌면서
// 방문하지 않았을 때
// 열 수 있으면 방문 check, total 누적, cnt 누적
// 모두 돌았을 때 (total / cnt) | 0

// if 방문 flag === false break