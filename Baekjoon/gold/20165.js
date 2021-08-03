// 백준 20165번 G5
// 인내의 도미노 장인 호석

const fs = require('fs')
// const stdin = fs.readFileSync('/dev/stdin').toString().split('\n')
const stdin = fs.readFileSync('input.txt').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const isInBound = (x, y, n, m) => {
  if (0 <= x && x < n && 0 <= y && y < m) return true
  return false
}

const falling = (array, used, x, y, d, n, m) => {
  let total = 0
  let dest_idx = 0
  let cx = x, cy = y
  while (isInBound(cx, cy, n, m) && dest_idx >= 0) {
    if (used[cx][cy] === 'S') {
      total++
      used[cx][cy] = 'F'

      const nDes =  array[cx][cy] - 1
      if (dest_idx < nDes) { // 쓰려뜨릴 영역이 더 길다면 이전보다 길다면
        dest_idx = nDes
      }
    }
    cx += d[0]
    cy += d[1]
    dest_idx--
  }

  return total
}

const round = (array, used, x, y, d, n, m) => {
  let total = 0

  if (d !== null) {  // 공격
    total += falling(array, used, x, y, d, n, m)
  } else { // 수비
    if (used[x][y] === 'F') {
      used[x][y] = 'S'
    }
  }
  return total
}

let total = 0
const [N, M, R] = input().split(' ').map(Number)
const array = new Array(N);
for (let i = 0; i < N; i++) {
  array[i] = input().split(' ').map(Number)
}
const used = Array.from(Array(N), () => new Array(M).fill('S'))
const dir = {E: [0, 1], W: [0, -1], S: [1, 0], N: [-1, 0]}
for (let i = 0; i < R * 2; i++) {
  const coor = input().split(' ')
  let x = y = d = null
  x = +coor[0] - 1
  y = +coor[1] - 1
  if (!(i % 2)) {  // 공격
    d = dir[coor[2]]
  }
  
  total += round(array, used, x, y, d, N, M)
}

console.log(total)
for (let i = 0; i < N; i++) {
  console.log(used[i].join(' '))
}

