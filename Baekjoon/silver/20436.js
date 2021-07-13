// 백준 20436번 S4
// ZOAC 3
// let stdin = fs.readFileSync('input.txt').toString().split('\n')

let fs = require('fs')
let stdin = fs.readFileSync('/dev/stdin').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const left = new Set(['q','w','e','r','t','a','s','d','f','g','z','x','c','v'])
const keyboard = [
  ['q','w','e','r','t','y','u','i','o','p'],
  ['a','s','d','f','g','h','j','k','l'],
  ['z','x','c','v','b','n','m']
]

// 알파벳별 키보드 좌표
const locations = Array(26).fill([])
for (let i = 0; i < keyboard.length; i++) {
  for (let j = 0; j < keyboard[i].length; j++) {
    const idx  = keyboard[i][j].charCodeAt(0) - 97
    locations[idx] = [i, j]
  }
}

// 알파벳을 아스키코드로 변환
const alphabetToAscii = (alphabet) => {
  return alphabet.charCodeAt(0) - 97
}

// 다음 타자 치는 시간 계산
const calcTime = (cx, cy, nx, ny) => {
  return Math.abs(cx-nx) + Math.abs(cy-ny)
}

// solution
const solution = (l, r, w) => {
  let [curr_lx, curr_ly] = locations[alphabetToAscii(l)]
  let [curr_rx, curr_ry] = locations[alphabetToAscii(r)]
  let total = 0

  for (let alpha of w) {
    const [next_x, next_y] = locations[alphabetToAscii(alpha)]

    if (left.has(alpha)) {
      total += calcTime(curr_lx, curr_ly, next_x, next_y)
      curr_lx, curr_ly = next_x, next_y
    } else {
      total += calcTime(curr_rx, curr_ry, next_x, next_y)
      curr_rx, curr_ry = next_x, next_y
    }
  }

  return total
}

const [l_start, r_start] = input().split(' ')
const word = input()
let res = solution(l_start, r_start, word)
res += word.length
console.log(res)
