// Leetcode no.104 easy
// Maximum Depth of Binary Tree

var maxDepth = function(root) {
  
  const dfs = (node, depth, res) => {
    if (!node) return res

    if (depth > res) {
      res = depth
    }

    res = dfs(node.left, depth+1, res)
    res = dfs(node.right, depth+1, res)

    return res
  }

  let res = 0
  res = dfs(root, 1, res)

  return res
};

const root = [3,9,20,null,null,15,7]
console.log(maxDepth(root))