// 백준 1138번 S2
// 한 줄로 서기

const fs = require('fs')
const stdin = fs.readFileSync('input.txt').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const solution = (N, array) => {
  const res = Array(N).fill(false)
  
  for (let i = 1; i < N+1; i++) {
    const k = array[i-1]

    let cnt = 0
    for (let j = 0; j < N; j++) {
      if (!res[j]) {
        if (cnt === k) {
          res[j] = i
          break
        }
        cnt++
      }
    }
  }
  return res
}

const N = +input()
const array = input().split(' ').map(Number)
const res = solution(N, array)
console.log(res.join(' '))
// 0 2 1 0
// each ele = false
// if !ele ? cnt++ then (cnt === k && !ele) ? array[i] = h
// ele < i ? 

// 1은 k 
// 2는 k or (1 ~ i-1 in 0~k count ? k + count)
// 2는 k or 

// 3은 1 or (1 ~ 2가 0~1까지에 count(1)개 있으므로 1 + 1)
