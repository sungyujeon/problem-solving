// Leetcode no.22 medium
// Generate Parentheses

// const generateParenthesis = (n) => {
//   const dpFunc = (m, dp) => {
//     if (m < 3 || dp[m] !== 0) {
//       return dp[m]
//     }
    
//     dp[m] = 2 * dp[m-1] + dp[m-2]
//     return dp[m]
//   }
  
//   const dp = new Array(9).fill(0)
//   dp[1] = 1
//   dp[2] = 2

//   return dpFunc(n, dp)
// }

const generateParenthesis = (n) => {
  const setParenthesis = (array, n) => {
    if (n < 3) return
    
    for (let i = 3; i < n+1; i++) {
    
        for (const pa of array[i-1]) {
          array[i].push('(' + pa + ')')
        }
      for (const pa of array[i-2]) {
        array[i].push(pa + '()()')
      }
    }
  }
  const array = Array.from(Array(9), () => [])
  array[1].push('()')
  array[2].push('(())', '()()')
  setParenthesis(n)
  console.log(array)
}

const n = 3
console.log(generateParenthesis(n))