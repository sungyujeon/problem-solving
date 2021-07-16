// 백준 1952번 B2
// 달팽이2

const fs = require('fs')
const stdin = fs.readFileSync('input.txt').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const solution = (m, n) => {
  const array = Array.from(Array(m), () => new Array(n).fill(0))
  const d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  let d_idx = 0
  let i = 0, j = 0
  let total = 0
  let res = 0

  while (true) {
    if (array[i][j] === 0) {
      array[i][j] = 1
      total++
    }
    
    if (total == m * n) {
      break
    }

    const ni = i + d[d_idx][0]
    const nj = j + d[d_idx][1]
    if (!(0 <= ni && ni < m) || !(0 <= nj && nj < n) || array[ni][nj] !== 0 ) {
      d_idx = (d_idx + 1) % 4
      i = i + d[d_idx][0]
      j = j + d[d_idx][1]
      res++
    } else {
      i = ni
      j = nj
    }
  }
  
  return res
}

const [M, N] = input().split(' ').map(Number)
const res = solution(M, N)
console.log(res)