const fs  = require('fs')
const stdin = fs.readFileSync('input.txt').toString().split('\n')


const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const heappush = (heap, ele) => {
  heap.push(ele)

  let idx = heap.length - 1

  while (idx > 0) {
    const parent = Math.trunc((idx - 1) / 2)

    if (heap[idx] < heap[parent]) {
      const tmp = heap[parent]

      heap[parent] = heap[idx]
      heap[idx] = tmp
      idx = parent
    } else {
      break
    }
  }
}

const findWord = (array, row, col, heap, flag) => {
  for (let i = 0; i < row; i++) {
    // 한줄을 검사하면서
    let idx = 0
    while (idx < col - 1) {
      let word = ''

      // 막혀있지 않을 때까지
      while (true) {

        if (flag) { // 가로
          if (array[i][idx] === '#' || array[i][idx] === undefined) {
            idx++
            break
          }
          word += array[i][idx]
          idx++
        } else { // 세로
          if (idx < col) { // 2차원 배열이라 예외 처리 해야
            if (array[idx][i] === '#' || array[idx][i] === undefined) {
              idx++
              break
            }
            word += array[idx][i]
            idx++
          } else {
            break
          }
        }
      }
      
      // 검사
      if (word.length > 1) {
        heappush(heap, word)
      }
    }
  }
}

const solution = (R, C, array) => {
  const res = []

  // 가로
  findWord(array, R, C, res, true)  

  // 세로
  findWord(array, C, R, res, false)

  return res
}

const [R, C] = input().split(' ').map(Number)
const array = Array.from(Array(R), () => input().split(''))
const res = solution(R, C, array)
console.log(res[0])