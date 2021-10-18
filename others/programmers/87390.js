// Programmers 월코챌3
// n^2 배열 자르기

function solution(n, left, right) {
  const res = []
  
  const startRow = parseInt((left+1) / n) - 1
  let cnt = startRow * n

  for (let i = startRow; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (cnt >= left && cnt <= right) {
        if (i > j) {
          res.push(i+1)
        } else {
          res.push(j+1)
        }
      }
      cnt++
      if (cnt > right) {
        return res
      }
    }
  }
}

const n = 4
const left = 7
const right = 14
console.log(solution(n, left, right))