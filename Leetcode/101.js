// Leetcode no.101 easy
// Symmetric Tree

// 같은 depth의 원소들을 대칭적으로 비교하며
// flag의 값을 false로 바꿔주는 전략을 택함
// vscode와 leetcode의 실행결과가 달라 당황스러움
// leetcode에서 input을 배열로 주는 것이 아니라
// child nodes를 갖는 객체 형태로 주어서 고려해야 풀어야 함

var isSymmetric = function(root) {
  const len = root.length
  let depth = 1
  let flag = true
  
  while (true) {
    let startIdx = (2 ** (depth-1)) - 1
    let endIdx = (2 ** depth) - 2
    if (!(startIdx < len)) break

    const midIdx = parseInt((startIdx + endIdx) / 2)
    for (let i = startIdx; i < midIdx + 1; i++) {
      const j = i - startIdx
      const rear = root[i]
      const tail = root[endIdx- j]
      
      if (rear !== tail) {
        flag = false
      }
    }
    depth++
  }

  return flag
};

// var isSymmetric = function(root) {
//   if (!root) return true

//   const tree = (left, right) => {
//     if (!left && !right) return true
//     if (!left || !right) return false
//     if (left.val !== right.val) return false

//     return tree(left.left, right.right) && tree(left.right, right.left)
//   }
  
//   return tree(root.left, root.right)
// }

const root = [1,2,2,null,3,null,3]
// const root = [1,2,2,3,4,4,3]
console.log(isSymmetric(root))

