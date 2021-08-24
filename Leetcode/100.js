// Leecode no.100 easy
// Same Tree

// 노드를 트리 형태로 순회하며 같은지 확인

var isSameTree = function(p, q) {
  
  const tree = (p, q, root, flag) => {
    if (p[root] === undefined || q[root] === undefined) return flag
    if (p[root] !== q[root]) {
      return false
    }

    const left = root * 2 + 1
    const right = root * 2 + 2

    flag = tree(p, q, left, flag)
    flag = tree(p, q, right, flag)

    return flag
  }

  let flag = true
  flag = tree(p, q, 0, flag)

  return flag
};

/* Leetcode의 input 형식이 단순 배열 형태로 주어지는 것이 아니라
 * left, right node 객체 형태로 주어져서
 * 실제 output이 다르게 나오는 점을 고려해야 함
*/
// var isSameTree = function(p, q) {
//   if (!p && !q) return true
//   if (!p || !q || p.val !== q.val) return false

//   return isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
// }


const p = [1,2]
const q = [1,null,2]

console.log(isSameTree(p, q))