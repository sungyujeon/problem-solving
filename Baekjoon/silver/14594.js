// 백준 14594번 S3
// 동방 프로젝트

// 배열을 1로 초기화
// 1로 초기화의 의미: n번째 방의 오른쪽에 벽이 있는지
// (n번 방의 마지막 오른쪽은 허물지 못하기 때문에 무조건 1)
// a ~ b 방의 벽을 허물면 array[a:b] = 0
// 1의 갯수 === 방의 갯수

// const stdin = fs.readFileSync('input.txt').toString().split('\n')
const fs = require('fs')
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const breakWall = (a, b, array) => {
  for (let i = a; i < b; i++) {
    if (array[i] === 1) {
      array[i] = 0
    }
  }
}

N = +input()
M = +input()
const array = Array(N).fill(1)
for (let i = 0; i < M; i++) {
  const [a, b] = input().split(' ').map(Number)
  breakWall(a-1, b-1, array)
}

const res = array.reduce((accum, value) => accum + value)
console.log(res)