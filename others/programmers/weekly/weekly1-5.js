// 첫번째 (5 ** 4) + (5 ** 3) + (5 ** 2) + 5

const vowel = ['A', 'E', 'I', 'O', 'U']

const dfs = (curr, depth, orders) => {
  if (depth > 5) {
    return
  }

  for (const v of vowel) {
    const next = curr + v
    orders.push(next)
    dfs(next, depth+1, orders)
  }
}


const solution = (word) => {
  const orders = []
  let res = 0

  dfs('', 1, orders)
  res = orders.indexOf(word) + 1
  
  return res
}

const word = 'EIO'
console.log(solution(word))