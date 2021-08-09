// 백준 16927번 S1
// 사다리 타기

// (N + M) * 2 - 4 번이 1 cycle
// 행렬을 -2씩 하면서 위 반복하면 cycle

const fs = require('fs')
const stdin = fs.readFileSync('input.txt').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const rotate = (i, j, row, col, array) => {
  let _i = i
  let _j = j

  let prev_num = 0
  while (_i < i+row) {
    const curr_num = array[_i][_j]
    if (_i != i) {
      array[_i][_j] = prev_num
      prev_num = curr_num
    } else {
      prev_num = curr_num
    }
    _i++
  }
  _i--
  _j++
  
  while (_j < j+col) {
    const curr_num = array[_i][_j]
    array[_i][_j] = prev_num
    prev_num = curr_num
    _j++
  }
  _j--
  _i--

  while (_i >= i) {
    const curr_num = array[_i][_j]
    array[_i][_j] = prev_num
    prev_num = curr_num
    _i--
  }
  _i++
  _j--

  while (_j >= j) {
    const curr_num = array[_i][_j]
    array[_i][_j] = prev_num
    prev_num = curr_num
    _j--
  }
}

const Square = (i, j, row, col, R, array) => {
  const cycle = (row + col) * 2 - 4
  const r = R % cycle

  for (let cnt = 0; cnt < r; cnt++) {
    rotate(i, j, row, col, array)
  }
}

const solution = (n, m, R, array) => {
  const last = Math.min(n, m) / 2

  for (let i = 0; i < last; i++) {
    const row = n - (2 * i)
    const col = m - (2 * i)
    Square(i, i, row, col, R, array)
  }
}

const [N, M, R] = input().split(' ').map(Number)
const array = Array.from(Array(N), () => input().split(' ').map(Number))
solution(N, M, R, array)

let res = ''
for (let i = 0; i < N; i++){
  res += array[i].join(' ') + '\n'
}
console.log(res)

