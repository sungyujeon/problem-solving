var inorderTraversal = function(root) {
  const res = []
  for (let i = 0; i < root.length+1; i++) {
    if (root[i] === null || root[i] === undefined) {
      let j = i - 1
      while (root[j]) {
        res.push(root[j])
        j--
      }
    }
  }
  return res
};

const root = [1, null, 2]
console.log(inorderTraversal(root))