// 백준 19948번 S3
// 음유시인 영재

const fs = require('fs')
const stdin = fs.readFileSync('input.txt').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const solution = (s, space, counts) => {
  counts[26] = space
  let i = 0

  while (true) {
    let idx = s[i].toLowerCase().charCodeAt(0) - 97
    idx = (idx === -65) ? 26 : idx

    if (counts[idx] < 1) {
      return -1
    } else {
      counts[idx]--
      i++
    }

    if (i >= s.length) {
      break
    }

    while (s[i] === s[i+1]) {
      i++
    }
    
  }

  return 1
}


const s = input()
const space = +input()
const counts = input().split(' ').map(Number)
const result = solution(s, space, counts)

let res = ''
if (result === 1) {
  const words = s.split(' ')
  for (const word of words) {
    if (!word) continue
    
    const idx = word[0].toLowerCase().charCodeAt(0) - 97
    if (counts[idx] < 1) {
      console.log(-1)
      break
    } else{
      counts[idx]--
      res += word[0].toUpperCase()
    }
  }
  console.log(res)
} else {
  console.log(result)
}