// 백준 14467번 S5
// 소가 길을 건너간 이유
// const stdin = fs.readFileSync('input.txt').toString().split('\n')

const fs = require('fs')
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const solution = (cow, loc, cows) => {
  const curr_loc = cows[cow]

  if (curr_loc === -1) {  // 처음 관찰한 소이면
    cows[cow] = loc
  } else if (curr_loc !== loc) {  // 이전 관찰했던 장소와 다르면
    cows[cow] = loc
    return 1
  }

  return 0
}

const N = Number(input())
const cows = Array(101).fill(-1)
let res = 0
for (let i = 0; i < N; i++) {
  const [cow, loc] = input().split(' ').map( (ele) => Number(ele) )
  res += solution(cow, loc, cows)
}

console.log(res)