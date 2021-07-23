// Leetcode no.6 medium
// ZigZag Conversion

// 내려갔다가 올라오는 규칙에 따라 배열 
//처음에 numRows가 1일 때의 예외가 생겨 틀렸는데 해당 부분을 고쳤습니다. 
//배열을 선언하여 문자를 할당하면 빈 배열이 많이 생겨 효율적이지 않을 것 같아 
//string을 합치는 방식으로 구현하였습니다. 그런데 string을 합치는 것도 과연 
//효율적인 것인가에 대한 의문이 생겨 찾아보니 아래와 같은 글이 있었습니다.

//https://stackoverflow.com/questions/7299010/why-is-string-concatenation-faster-than-array-join
// 내용을 보면 V8 engine 알고리즘상 string concatenation이 array join 보다 속도가 빠르다고 합니다. 
// 는 C++로 돌아가는 concatenation의 경우 StringBuilderConcat 함수를 호출하여 문자열을 합치기 때문이라고 보았습니다.

var convert = function(s, numRows) {
  if (numRows === 1) return s

  const strArray = Array(numRows).fill('')

  let row = 0
  let flag = true
  for (let i = 0; i < s.length; i++) {
    strArray[row] += s[i]

    if (flag) { // 아래로
      if (row === numRows-1) {
        flag = !flag
        row--
      } else {
        row++
      }
    } else {
      if (row === 0) {
        flag = !flag
        row++
      } else {
        row--
      }
    }
  }
  return strArray.join('')
}

const s = 'PAYPALISHIRING'
const numRows = 3
console.log(convert(s, numRows))