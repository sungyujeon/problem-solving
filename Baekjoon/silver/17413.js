// 백준 17413번 S3
// 단어 뒤집기 1

const fs = require('fs')
const stdin = fs.readFileSync('input.txt').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const solution = (s) => {
  let res = ''
  let n = s.length
  let i = 0
  while (i < n) {
    const char = s.charAt(i)
    
    if (char === '<') {
      while (true) {
        const _char = s.charAt(i)
        res += _char
        i++

        if (_char === '>') break  
      }
    } else {
      let tmpS = ''
      while (true) {
        const _char = s.charAt(i)
        
        if (!_char || _char === '<' || _char == ' ') {
          res += tmpS

          if (_char === ' ') {
            res += ' '
            i++
          }
          break
        } else {
          tmpS = _char + tmpS
          i++
        }
      }
    }
  }

  return res
}

const S = input()
console.log(solution(S))

