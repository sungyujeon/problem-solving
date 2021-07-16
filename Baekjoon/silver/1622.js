// 백준 1622번 S4
// 공통 순열
// const stdin = fs.readFileSync('input.txt').toString().split('\n')

const fs = require('fs')
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const solution = (a, b) => {
  let res = ''
  const arrayA = Array(26).fill(0)
  const arrayB = Array(26).fill(0)
  
  for (let i = 0; i < a.length; i++) {
    const idx = a.charCodeAt(i) - 97
    arrayA[idx]++
  }

  for (let i = 0; i < b.length; i++) {
    const idx = b.charCodeAt(i) - 97
    arrayB[idx]++
  }

  for (let i = 0; i < 26; i++) {
    const num1 = arrayA[i]
    const num2 = arrayB[i]
    
    if (num1 && num2) {
      const cnt = Math.min(num1, num2)
      
      for (let j = 0; j < cnt; j++) {
        res += String.fromCharCode(i + 97)
      }
    }
  }

  return res
}

while (1) {
  let A = input()
  let B = input()
  
  if (A === undefined || B === undefined) break
  if (A == '' || B == '') {
    console.log('')
    continue
  }
  
  const res = solution(A, B)
  console.log(res)
}