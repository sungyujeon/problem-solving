// Programmers
// 타겟 넘버

function solution(numbers, target) {
  let res = 0
  const dfs = (curr, depth, n, _numbers, target) => {
    if (depth === n) {
      if (curr === target) {
        res += 1
      }
      return
    }

    for (let i = 0; i < 2; i++) {
      if (i % 2) {
        dfs(curr + _numbers[depth], depth + 1, n, _numbers, target)
      } else {
        dfs(curr - _numbers[depth], depth + 1, n, _numbers, target)
      }
    }
  }

  const n = numbers.length
  dfs(0, 0, n, numbers, target) 
  
  return res
}

const numbers = [1,1,1,1,1]
const target = 3
console.log(solution(numbers, target))