// 프로그래머스 월코챌3
// 나머지가 1이 되는 수 찾기

function solution(n) {
  for (let i = 2; i < n; i++) {
    if ((n-1) % i === 0) {
      return i
    }
  }
}

console.log(solution(10))