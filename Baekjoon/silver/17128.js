// 백준 17128번 S2
// 소가 정보섬에 올라온 이유

const fs = require('fs')
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const change_sum = (idx, sum, sum_array, N) => {
  let _sum = sum
  for (let i = idx-3; i <= idx; i++) {
    let _i = (i < 0) ? i+N : i
    const _num = sum_array[_i] * (-1)

    sum_array[_i] = _num
     _sum += _num * 2
  }
  return _sum
}

const make_sum = (scores, N) => {
  const array = Array(N).fill(0)

  for (let i = 0; i < N; i++) {
    array[i] = scores[(i % N)] * scores[((i+1) % N)] * scores[((i+2) % N)] * scores[((i+3) % N)]
  }

  return array
}

const solution = (N, scores, cow_numbers) => {
  const sum_array = make_sum(scores, N)
  let sum = sum_array.reduce((acc, value) => acc + value)
  const res = []

  for (let cow_num of cow_numbers) {
    sum = change_sum(cow_num-1, sum, sum_array, N)
    res.push(sum)
  }
  return res
}


const [N, Q] = input().split(' ').map(Number)
const scores = input().split(' ').map(Number)
const cow_numbers = input().split(' ').map(Number)

const res = solution(N, scores, cow_numbers)
console.log(res.join('\n'))