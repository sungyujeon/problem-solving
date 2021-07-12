// const stdin = fs.readFileSync('input.txt').toString().split('\n')
const fs = require('fs')
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const move = (x, y, dir) => {
  x += dir[0]
  y += dir[1]
  return [x, y]
}

const solution = (n, m) => {
  const array = Array.from(Array(n), () => Array(n).fill(0))
  let res_ij = []
  const share = parseInt(n / 2)

  const directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
  let direction = 0
  let cnt = 1
  let number = 1
  let i = share
  let j = share
  
  
  while (number < n ** 2 + 1) {
    array[i][j] = number
    
    if (Number.isInteger(number ** (1/2))) {
      [i, j] = move(i, j, directions[direction])
      cnt++
      number++
    } else {
      direction = (direction + 1) % 4
      for (let k = 0; k < (cnt - 1) * 2; k++) {
        if (k === cnt - 1) {
          direction = (direction + 1) % 4
        }
        [i, j] = move(i, j, directions[direction])
        number++
        array[i][j] = number

        if (number === m) {
          res_ij = [i+1, j+1]
        }
      }
    }

    if (number === m) {
      res_ij = [i+1, j+1]
    }

  }

  return [array, res_ij]

}


N = +input()
M = +input()
const res = solution(N, M)

for (let arr of res[0]) {
  console.log(...arr)
}
console.log(...res[1])